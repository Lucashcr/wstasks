import os

from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.environ["SECRET_KEY"]

CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = os.environ["CELERY_RESULT_BACKEND"]

REDIS_CONNECTION = {
    "host": os.environ["REDIS_HOST"],
    "port": int(os.environ["REDIS_PORT"]),
    "db": os.environ["REDIS_DB"],
}
