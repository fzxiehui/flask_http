import jwt
import datetime

from app.utils.response import error

SECRET_KEY = "your-secret-key"

def generate_token(user):
    payload = {
        "id": user.id,
        "username": user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # 过期时间
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token



def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # token过期
    except jwt.InvalidTokenError:
        return None  # 非法token

from functools import wraps
from flask import request
from flask import g

def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  # Bearer token
        if not token:
            return error(msg="Token missing", code=401)
        
        data = decode_token(token)
        if not data:
            return error(msg="Invalid or expired token", code=401)
        
        # 这里把 user.id 和 user.username 都放进 g 对象，方便后续使用
        g.user_id = data["id"]
        g.username = data["username"]
        
        return func(*args, **kwargs)
    return decorated
