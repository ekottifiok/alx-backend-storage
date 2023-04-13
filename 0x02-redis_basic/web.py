#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
from redis import Redis
from functools import wraps
from typing import Callable

redis = Redis()


def check_cache(f: Callable) -> Callable:
    """Checks the cache if the webpage is stored there"""
    @wraps(f)
    def wrapper(url: str) -> str:
        """
        wrapper preserves the functions documentation and
        function name
        """
        redis.incr("count:{}".format(url))
        web_page = redis.get(url)
        if web_page:
            return web_page.decode("utf-8")
        web_page = f(url)
        redis.set(url, f(url), 10)
        redis.set("count:{}".format(url), 0)
        return web_page

    return wrapper


@check_cache
def get_page(url: str) -> str:
    """
    In this tasks, we will implement a get_page function (prototype: def
    get_page(url: str) -> str:). The core of the function is very simple. 
    It uses the requests module to obtain the HTML content of a particular
    URL and returns it.

    Start in a new file named web.py and do not reuse the code written in
    exercise.py.

    Inside get_page track how many times a particular URL was accessed in
    the key "count:{url}" and cache the result with an expiration time of
    10 seconds.

    Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response
    and test your caching.

    Bonus: implement this use case with decorators.
    """

    from requests import get
    return get(url).text
