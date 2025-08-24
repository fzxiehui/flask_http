from app.models import User, db
from datetime import datetime



class UserService(object):

    @staticmethod
    def register(username, password):

        if User.query.filter_by(username=username).first():
            raise Exception("username already exists")

        user = User(username=username)
        user.set_password(password=password)
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def login(username, password) -> User:
        
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            raise Exception("Username or Password Error!")

        return user
