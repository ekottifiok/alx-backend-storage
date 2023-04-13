#!/usr/bin/env python3
"""Cache module"""
from redis import Redis
from uuid import uuid4
from typing import Any, Callable, Union
from functools import wraps


def count_calls(f: Callable) -> Callable:
    """Calculates how many times the function is called"""
    @wraps(f)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        wrapper preserves the functions documentation and
        function name
        """
        if isinstance(self._redis, Redis):
            self._redis.incr(f.__qualname__)
        return f(self, *args, **kwargs)
    return wrapper


def call_history(f: Callable) -> Callable:
    """
    Everytime the original function will be called, we will
    add its input parameters to one list in redis, and store 
    its output into another list.
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        wrapper preserves the functions documentation and
        function name
        """
        f_ret = f(self, *args, **kwargs)
        if isinstance(self._redis, Redis):
            self._redis.rpush(
                '{}:inputs'.format(f.__qualname__),
                str(args)
            )
            self._redis.rpush(
                '{}:outputs'.format(f.__qualname__),
                f_ret
            )
        return f_ret
    return wrapper


def replay(f: Callable) -> None:
    """
    In this tasks, we will implement a replay function to display the
    history of calls of a particular function.

    Use keys generated in previous tasks to generate the following output:
    """
    if f is None or not hasattr(f.__self__, '_redis'):
        return
    store = getattr(f.__self__, '_redis', None)
    if not isinstance(store, Redis):
        return
    func_name = f.__qualname__
    inputs = '{}:inputs'.format(func_name)
    outputs = '{}:outputs'.format(func_name)

    print('{} was called {} times:'.format(
        func_name,
        0 if store.exists(func_name) != 0 and
        not store.get(func_name) else store.get(func_name)
    ))
    func_inputs = store.lrange(inputs, 0, -1)
    func_outputs = store.lrange(outputs, 0, -1)
    for input, output in zip(func_inputs, func_outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            input.decode('utf-8'),
            output
        ))


class Cache:
    """
    Class implements the redis caching
    """

    def __init__(self) -> None:
        self._redis = Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Stores data in a redis cache"""
        data_id = str(uuid4())
        self._redis.set(data_id, data)
        return data_id

    def get(self, key: str, **kwargs) -> (Union[str, int, float, bytes, None]):
        """Retrieves data from the cache"""
        data = self._redis.get(key)
        func = kwargs.get("fn", None)
        return func(data) if func is not None else data

    def get_str(self, key: str):
        """
        Calls the internal get and passes
        in a function to convert to str
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """
        Calls the internal get and 
        passes in a function to convert to int
        """
        return self.get(key, fn=lambda d: int(d))
