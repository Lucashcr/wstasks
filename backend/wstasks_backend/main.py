from fastapi import FastAPI
import uvicorn

from wstasks_backend.config.middlewares.cors import setup_cors_middleware
from wstasks_backend.config.celery import make_celery
from wstasks_backend.lifespan import lifespan
from wstasks_backend.router import setup_router

app = FastAPI(lifespan=lifespan)

setup_cors_middleware(app)

setup_router(app)

celery = make_celery()


if __name__ == "__main__":
    uvicorn.run("wstasks_backend.main:app", host="127.0.0.1", port=8000)
