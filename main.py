from app import create_app
from app.ws import socketio
import eventlet
import eventlet.wsgi

if __name__ == "__main__":

    app = create_app()
    # app.run()
    # socketio.run(app=app, debug=True)
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False,   # 可选：避免多进程冲突
    )
