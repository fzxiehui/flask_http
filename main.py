from app import create_app
from app.ws import socketio


if __name__ == "__main__":

    app = create_app()
    # app.run()
    socketio.run(app=app, debug=True)
