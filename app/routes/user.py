from flask import Blueprint, g, request

from app.services.user import UserService
from app.utils.decorators import handle_exceptions, require_json
from app.utils import generate_token
from app.utils.jwt import login_required
from app.utils.response import success

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
@handle_exceptions
@require_json
def register():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")
    print("debug")

    if not username or not password:
        raise Exception("username and password cannot be empty!")

    UserService.register(username=username, password=password)
    return success(msg="register success")

@auth_bp.route("/login", methods=["POST"])
@handle_exceptions
@require_json
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    assert len(username) > 1, Exception("Username cannot be empty")
    assert len(password) > 1, Exception("Password cannot be empty")

    user = UserService.login(username=username, password=password)
    print(user)
    token = generate_token(user)
    print(token)
    res = {
            "username": user.username,
            "token": token,
    }
    
    return success(data=res)

@auth_bp.route("/login_required", methods=["POST"])
@handle_exceptions
@login_required
def login_required():

    res = {
            "id": g.get("user_id"),
            "username": g.get("username"),
            }
    return success(data=res)
