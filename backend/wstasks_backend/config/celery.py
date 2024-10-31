from functools import lru_cache

from celery import Celery

from wstasks_backend.config import settings


@lru_cache
def make_celery() -> Celery:
    celery = Celery(
        __name__,
        broker=settings.CELERY_BROKER_URL,
        backend=settings.CELERY_RESULT_BACKEND,
        broker_connection_retry_on_startup=True,
    )

    return celery
