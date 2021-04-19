from marshmallow import fields

from app import ma
from app.models import User, Section, Thread, Post


class UserListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True


user_list_schema = UserListSchema(many=True)


class SectionListSchema(ma.SQLAlchemySchema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    tag = fields.String()
    thread_count = fields.Integer()
    post_count = fields.Integer()
    created_dt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')

    class Meta:
        model = Section
        include_fk = True


section_list_schema = SectionListSchema(many=True)


class ThreadListSchema(ma.SQLAlchemySchema):
    id = fields.Integer()
    name = fields.String()
    section_id = fields.Integer()
    views = fields.Integer()
    username = fields.String()
    post_count = fields.Integer()
    created_dt = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')

    class Meta:
        model = Thread
        include_fk = True


thread_list_schema = ThreadListSchema(many=True)


class PostListSchema(ma.SQLAlchemySchema):
    id = fields.Integer()
    text = fields.String()
    created = fields.DateTime(format='%Y-%m-%d %H:%M:%S%z')
    thread_id = fields.Integer()
    username = fields.String()

    class Meta:
        model = Post
        include_fk = True


post_list_schema = PostListSchema(many=True)


# from babel.dates import format_date, format_datetime, format_time
# format_datetime(dt, "EEE, d MMMM yyyy, H:mm", locale='ru')
