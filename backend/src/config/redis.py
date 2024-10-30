from functools import lru_cache

from redis import Redis

from config.settings import REDIS_CONNECTION


@lru_cache
def make_redis() -> Redis:
    return Redis(**REDIS_CONNECTION)
