import uuid
import random
import string
from cachetools import TTLCache
import threading

from app.utils import SingletonMeta


PASSWORD_LENGTH = 8
TTL_SECONDS = 60 * 1
MAX_CACHE_SIZE = 1000

class WsAuth(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.__cache = TTLCache(maxsize=MAX_CACHE_SIZE, ttl=TTL_SECONDS)
        self.__chars = string.ascii_letters + string.digits
        self.__lock = threading.Lock()


    def generate_token(self, userinfo = None) -> tuple[str, str]:
        """
            生成临时登录授权, 前端websocket通过 
                url?key=xxx&password=xxx 带到服务端

            Args:
                userinfo: 用户信息,可以是dict, str等, 
                    通过check认证成功后会返回该信息

            Returns:
                key: 密码键
                password: 密码键
        """
        try:
            self.__lock.acquire()
            password = self.__generate_password()
            key = self.__generate_key()
            cache_data = {
                    "password": password,
                    "userinfo": userinfo,
            }
            self.__cache[key] = cache_data
            return key, password
        finally:
            self.__lock.release()

    def check(self, key, password):
        """
            校验身份是否正确, 如正确返回用户信息

            Args:
                key: 密码键
                password: 密码键

            Returns:
                userinfo: 在调用 generate_token 函数时传入的用户信息

            Raises:
                验证失败
        """
        with self.__lock:
            data = self.__cache.pop(key, None)
        
        assert data is not None, Exception("illegal request")

        if password != data["password"]:
            raise Exception("illegal request")

        return data["userinfo"]


    def __generate_password(self) -> str:
        num = uuid.uuid4().int
        result = []
        while num:
            num, rem = divmod(num, 62)
            result.append(self.__chars[rem])
        return ''.join(result)[:8]  # 截取8位短密码


    def __generate_key(self) -> str:
        while True:
            key = ''.join(random.choices(self.__chars, k=PASSWORD_LENGTH))
            if key not in self.__cache:
                return key
