from requests import get
from redis import Redis

redis = Redis()
key = "web_page"


def get_page(url: str) -> str:

    web_page = redis.get(key)
    web_page = web_page.decode() if web_page else redis.set(key, get(url).text, 10)
    return str(web_page)
