"""
    以下脚本用于自动创建sqlite文件
    在创建了 Flask app 并进行 
        db.init_app(app)
        migrate.init_app(app)
        后使用
"""
import os
from flask_migrate import upgrade

def init_db(app):
    """检查 SQLite 是否存在，如果不存在则自动迁移"""
    db_uri = app.config["SQLALCHEMY_DATABASE_URI"]

    # 只处理 sqlite:/// 
    if db_uri.startswith("sqlite:///"):
        db_file = db_uri.replace("sqlite:///", "")
        if not os.path.exists(db_file):
            print(f"[DB] 数据库文件 {db_file} 不存在，正在自动迁移...")
            try:
                with app.app_context():
                    upgrade()
            except Exception as e:
                print(e)
        else:
            print(f"[DB] 数据库文件 {db_file} 已存在，跳过迁移")
