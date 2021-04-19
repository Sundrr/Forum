import datetime
import jwt

from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db


JWT_SECRET = app.config.get('SECRET_KEY')


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visited = db.Column(db.DateTime)
    avatar = db.Column(db.String(120))
    subscript = db.Column(db.String(240))
    posts = relationship('Post', back_populates='author')
    threads = relationship('Thread', back_populates='creator')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def encode_auth_token(user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),  # expires
                'iat': datetime.datetime.utcnow(),  # issued at
                'sub': user_id
            }
            return jwt.encode(
                payload,
                JWT_SECRET,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, JWT_SECRET, algorithm='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class Section(db.Model):
    __tablename__ = 'section'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(200))
    tag = db.Column(db.String(10))
    threads = relationship('Thread', back_populates='section')

    def __repr__(self):
        return '<Section {}>'.format(self.id)


class Thread(db.Model):
    __tablename__ = 'thread'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creator = relationship('User', back_populates='threads')
    views = db.Column(db.Integer, default=0)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    section = relationship('Section', back_populates='threads')
    posts = relationship('Post', back_populates='thread')


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', back_populates='posts')
    text = db.Column(db.String(240))
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    thread = relationship('Thread', back_populates='posts')

# from sqlalchemy.dialects.postgresql import JSON
# result_no_stop_words = db.Column(JSON)

