# from flask import jsonify
# 
# def success(data=None, msg="ok", code=200):
#     return jsonify({
#         "code": code,
#         "msg": msg,
#         "data": data
#     }), code
# 
# def error(msg="error", code=400, data=None):
#     return jsonify({
#         "code": code,
#         "msg": msg,
#         "data": data
#     }), code
import json
from flask import Response

def success(data=None, msg="ok", code=200):
    return Response(
        json.dumps({"code": code, "msg": msg, "data": data}, ensure_ascii=False),
        mimetype="application/json"
    ), code

def error(msg="error", code=400, data=None):
    return Response(
        json.dumps({"code": code, "msg": msg, "data": data}, ensure_ascii=False),
        mimetype="application/json"
    ), code
