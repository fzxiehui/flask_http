import unittest
import requests


BASE_URL = "http://127.0.0.1:5000"

class TestUser(unittest.TestCase):


    def test_user(self) -> None:

        res = requests.post(f"{BASE_URL}/auth/register", json={
            "username": "root",
            "password": "root",
            })

        print(res)

        res = requests.post(f"{BASE_URL}/auth/login",
                json={
                        "username": "root",
                        "password": "root",
                })

        assert res.status_code == 200
        print(res.json())

        token = res.json().get("data").get("token")
        print(token)
        headers = {
            "Authorization": f"Bearer {token}"
        }
        res = requests.get(f"{BASE_URL}/auth/get_ws_token",
                           headers=headers)

        print(res.json())
