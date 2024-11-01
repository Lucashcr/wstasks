from redis import Redis

from wstasks_backend.config.settings import REDIS_CONNECTION


redis = Redis(**REDIS_CONNECTION)
