from flask import Blueprint, g, request

from app.services import UserService
from app.utils.decorators import handle_exceptions, require_json
from app.utils import generate_token
from app.utils import login_required
from app.utils.response import success
from app.ws import WsAuth

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

ws_auth = WsAuth()


@auth_bp.route("/register", methods=["POST"])
@handle_exceptions
@require_json
def register():
    data = request.json
    username = data.get("username", "")
    password = data.get("password", "")

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
    token = generate_token(user)
    res = {
            "username": user.username,
            "token": token,
    }
    
    return success(data=res)

@auth_bp.route("/login_required", methods=["POST"])
@handle_exceptions
@login_required
def login_required_route():

    res = {
            "id": g.get("user_id"),
            "username": g.get("username"),
            }
    return success(data=res)

@auth_bp.route("/get_ws_token", methods=["get"])
@handle_exceptions
@login_required
def get_ws_token():

    userinfo = {
            "id": g.get("user_id"),
            "username": g.get("username"),
            }
    key, password = ws_auth.generate_token(userinfo=userinfo)
    res = {
            "key": key,
            "password": password,
    }
    return success(data=res)
