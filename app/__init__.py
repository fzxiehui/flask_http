from flask import Flask
from .routes import register_routes
from flask_migrate import Migrate
from app.models import db
from flask_cors import CORS

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # 跨域支持（允许所有来源）
    CORS(app, resources={r"/*": {"origins": "*"}})

    # app.config['SECRET_KEY'] = 'chat-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    register_routes(app)

    return app
