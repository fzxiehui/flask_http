from datetime import datetime
from . import db


class TestUser(db.Model):
    __tablename__ = 'test_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
