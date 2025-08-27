import logging
import unittest
from app.ws import WsAuth


class TestWsAuth(unittest.TestCase):


    def test_auth(self) -> None:

        auth = WsAuth()
        for i in range(20):
            key, password = auth.generate_token(userinfo={
                "id": i,
                })
            print("key:", key)
            print("password:", password)

            userinfo = auth.check(key=key, password=password)
            print(userinfo)

        try:
            auth.check(key="testkey", password="testpassword")
        except Exception as e:
            print("错误测试:", e)
            
