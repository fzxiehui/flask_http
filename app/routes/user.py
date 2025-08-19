from flask import Blueprint, request

from app.services.user import UserService
from app.utils.decorators import handle_exceptions, require_json
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
