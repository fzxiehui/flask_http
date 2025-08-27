import threading

# 单例模式
class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()  # 用于线程安全地创建单例

    def __call__(cls, *args, **kwargs):
        # 第一次判断，不加锁，提高性能
        if cls not in cls._instances:
            with cls._lock:
                # 第二次判断，加锁后防止并发创建
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# 单例模式, 与上面不同的是,当参数不一样时会创建新的对象
class ParametrizedSingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # 用参数生成唯一key（注意必须可哈希）
        key = (cls, args, frozenset(kwargs.items()))

        if key not in cls._instances:
            with cls._lock:
                if key not in cls._instances:
                    cls._instances[key] = super().__call__(*args, **kwargs)
        return cls._instances[key]
