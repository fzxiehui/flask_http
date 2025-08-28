from flask_socketio import Namespace, emit

class Chat(Namespace):
    def on_connect(self):
        print("Client connected to ChatNamespace")
        emit('message', {'data': 'Welcome to Chat!'})

    def on_message(self, data):
        print("Received message:", data)
        emit('message', {'data': data}, broadcast=True)
