from .testuser import test_bp
from .user import auth_bp


def register_routes(app):
    app.register_blueprint(test_bp)
    app.register_blueprint(auth_bp)
