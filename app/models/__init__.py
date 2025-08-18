from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .test_user import TestUser


__all__ = [
        "db",
        "TestUser"
        ]
