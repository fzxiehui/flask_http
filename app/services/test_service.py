from app.models import db, TestUser
from datetime import datetime

class TestUserService(object):

    def store_user(username):
        user = TestUser(username=username, timestamp=datetime.utcnow())
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_users(limit=100):
        messages = TestUser.query.order_by(TestUser.timestamp.desc()).limit(limit).all()
        return [
            {
                'username': m.username,
                'timestamp': m.timestamp.isoformat() + 'Z'
            }
            for m in reversed(messages)
        ]
