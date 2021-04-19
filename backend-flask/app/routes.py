import json

from sqlalchemy import func, or_

from flask import make_response, request, jsonify

from app import app, session, db
from app.models import User, Section, Thread, Post
from app.serializers import user_list_schema, section_list_schema, thread_list_schema, post_list_schema

from app.utils import authorized


@app.route('/auth/register', methods=['POST'])
def register():
    """
    Регистрирует нового пользователя
    """
    data = request.json
    user = session.query(User)\
        .filter(or_(User.email == data.get('email'), User.username == data.get('username'))).first()
    if not user:
        user = User(
            username=data.get('username'),
            email=data.get('email'),
        )
        user.set_password(data.get('password'))
        session.add(user)
        session.commit()
        auth_token = user.encode_auth_token(user.id)
        response = 'Bearer ' + auth_token
        return make_response(jsonify(response), 201)
    else:
        response = 'User already exists. Please Log in'
        return make_response(jsonify(response), 400)


@app.route('/auth/login', methods=['POST'])
def login():
    """
    Авторизует пользователя
    """
    data = request.json
    user = session.query(User).filter_by(username=data.get('username')).first()
    if user and user.check_password(data.get('password')):
        auth_token = user.encode_auth_token(user.id)
        response = 'Bearer ' + auth_token
        return make_response(response, 200)
    else:
        return make_response('Wrong authorization data', 400)


@app.route('/users/full_list')
def user_full_list():
    """
    Возвращает полный список пользователей
    """
    users = session.query(User).all()
    response = user_list_schema.dump(users)
    json_response = jsonify(response)
    return make_response(json_response, 200)


@app.route('/sections/full_list')
def section_full_list():
    """
    Возвращает полный список разделов с подсчетом количества групп и постов в каждом разделе, а также выводит данные
    по последнему пользователю, написавшему пост в данном разделе
    """
    max_dt_query = session.query(
        Post.thread_id,
        Post.author,
        func.max(Post.created).label('created_dt'),
        User.username
    ).join(User).group_by(Post.thread_id).subquery().alias('max_dt_query')

    post_subquery = session.query(
        Post.thread_id,
        func.count('*').label('count'),
        max_dt_query.c.created_dt,
        max_dt_query.c.username
    ).outerjoin(max_dt_query, Post.thread_id == max_dt_query.c.thread_id)\
        .group_by(Post.thread_id).subquery().alias('post_subquery')

    thread_subquery = session.query(
        Thread.section_id,
        func.count('*').label('thread_count'),
        func.sum(post_subquery.c.count).label('post_count'),
        post_subquery.c.created_dt,
        post_subquery.c.username
    ).outerjoin(post_subquery).group_by(Thread.section_id).subquery()

    queryset = session.query(
        Section.id,
        Section.name,
        Section.description,
        Section.tag,
        thread_subquery.c.thread_count,
        thread_subquery.c.post_count,
        thread_subquery.c.created_dt,
        thread_subquery.c.username
    ).outerjoin(thread_subquery)
    response = section_list_schema.dump(queryset)
    json_response = jsonify(response)
    return make_response(json_response, 200)


@app.route('/threads/<int:section_id>')
def section_thread_list(section_id):
    """
    Возвращает список тем для выбранного раздела с подсчетом количества ответов и просмотров, а также выводит данные
    по последнему пользователю, написавшему пост в данном разделе
    """
    max_dt_query = session.query(
        Post.thread_id,
        Post.author,
        func.max(Post.created).label('created_dt'),
        User.username
    ).join(User).group_by(Post.thread_id).subquery().alias('max_dt_query')

    post_subquery = session.query(
        Post.thread_id,
        func.count('*').label('post_count'),
        max_dt_query.c.created_dt,
        max_dt_query.c.username
    ).outerjoin(max_dt_query, Post.thread_id == max_dt_query.c.thread_id)\
        .group_by(Post.thread_id).subquery().alias('post_subquery')

    queryset = session.query(
        Thread.id,
        Thread.name,
        Thread.created,
        Thread.section_id,
        Thread.views,
        post_subquery.c.post_count,
        post_subquery.c.created_dt,
        post_subquery.c.username
    ).outerjoin(post_subquery).filter(Thread.section_id == section_id).order_by(Thread.created.desc())
    response = thread_list_schema.dump(queryset)
    json_response = jsonify(response)
    return make_response(json_response, 200)


@app.route('/posts/<int:thread_id>')
def thread_post_list(thread_id):
    """
    Возвращает список постов для выбранной темы
    """
    page = request.args.get('page', 1, type=int)
    thread = db.session.query(Thread).get(thread_id)
    thread.views += 1
    session.commit()
    queryset = db.session.query(
        Post.id,
        Post.text,
        Post.created,
        Post.thread_id,
        User.username
    ).outerjoin(User)\
        .filter(Post.thread_id == thread_id)\
        .order_by(Post.created.desc())\
        .paginate(page, app.config['POST_PER_PAGE'], False)
    response = {
        'data': post_list_schema.dump(queryset.items),
        'pages_total': queryset.pages,
        'page': queryset.page,
        'total': queryset.total
    }
    json_response = jsonify(response)
    return make_response(json_response, 200)


@app.route('/threads/create', methods=['POST'])
@authorized
def create_post(user_id):
    """
    Создает новую тему и первый пост в ней
    """
    data = request.json
    section_id = data.get('section_id')
    thread_id = data.get('thread_id')
    thread_name = data.get('thread_name')
    text = data.get('text')

    if not thread_id:
        thread = Thread(
            name=thread_name,
            user_id=user_id,
            views=0,
            section_id=section_id
        )
        session.add(thread)
        session.commit()
        thread_id = thread.id

    post = Post(
        user_id=user_id,
        text=text,
        thread_id=thread_id
    )
    session.add(post)
    session.commit()
    return make_response(str(thread_id), 201)


if __name__ == '__main__':
    app.run()

