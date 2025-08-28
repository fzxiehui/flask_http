
from .auth import WsAuth
from .chat import Chat

from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")

socketio.on_namespace(Chat('/chat'))

__all__ = [
        "socketio",
        "WsAuth"
        ]

