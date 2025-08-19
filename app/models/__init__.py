from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .test_user import TestUser
from .user import User


__all__ = [
        "db",
        "TestUser",
        "User"
        ]
