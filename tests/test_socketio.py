import unittest
from engineio.client import time
import socketio


class TestSocketIO(unittest.TestCase):

    def test_chat(self) -> None:

        print(__name__)

        sio = socketio.Client()


        @sio.event
        def connect():
            print("connect")

        @sio.on("message", namespace="/chat")
        def on_message(data):
            print("on_message", data)

        @sio.event
        def disconnect():
            print("disconnect")

        sio.connect("http://127.0.0.1:5000")

        sio.emit("chat", "hello")

        sio.wait()
