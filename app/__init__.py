from flask import Flask
from flask import send_from_directory
from .routes import register_routes
from flask_migrate import Migrate
from app.models import db
from flask_cors import CORS

migrate = Migrate()

def create_app():
    app = Flask(
            import_name=__name__,
            static_folder="webui",       # Vue 静态文件目录
            static_url_path=""           # 静态资源直接从根路径访问
            )

    # 跨域支持（允许所有来源）
    CORS(app, resources={r"/*": {"origins": "*"}})

    # app.config['SECRET_KEY'] = 'chat-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    register_routes(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve_vue(path):
        if path != "" and (app.static_folder / path).exists():
            # 如果请求的是静态文件，直接返回
            return send_from_directory(app.static_folder, path)
        else:
            # 不是静态文件 → 返回 index.html (交给 Vue Router 处理)
            return send_from_directory(app.static_folder, "index.html")

    return app
