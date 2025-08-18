from flask import Blueprint, request, jsonify
from app.services import TestUserService

test_bp = Blueprint('test', __name__, url_prefix='/test')

@test_bp.route('/users', methods=['GET'])
def get_history():
    messages = {
            "messages": TestUserService.get_users()
            }
    return jsonify(messages)


@test_bp.route("/adduser", methods=["POST"])
def add_user():
    data = request.json
    username = data.get("username", None)
    TestUserService.store_user(username)
    return jsonify({
        "code": 0,
        "msg": "",
        "data": ""
        })
