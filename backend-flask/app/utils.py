import jwt
from functools import wraps

from flask import request, make_response

from app import app


JWT_SECRET = app.config.get('SECRET_KEY')


def authorized(f):
    """
    Декоратор для защиты доступа к контроллеру от неавторизованных пользователей
    """
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'Authorization' not in request.headers:
            return make_response('Доступ запрещен', 403)

        data = request.headers['Authorization']
        token = str.replace(str(data), 'Bearer ', '')
        try:
            user_id = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
            return f(user_id, *args, **kws)
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        except Exception as e:
            print(str(e))
            return make_response(str(e), 400)

    return decorated_function

