from functools import wraps
from flask import request
from .response import error

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # @TODO: log
            return error(msg=str(e), code=500)
    return wrapper

def require_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return error(msg="Requests must be in JSON format.", code=415)
        return func(*args, **kwargs)
    return wrapper
