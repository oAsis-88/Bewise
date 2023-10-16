from threading import Lock


class SingletonMultithreadBaseClass(type):
    """
    - Класс, который имеет только один экземпляр.
    - Для мультипоточной работы.

    Пример:

    >>> class MyClass(metaclass=SingletonMultithreadBaseClass): ...
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]