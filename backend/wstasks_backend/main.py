from fastapi import FastAPI
import uvicorn

from wstasks_backend.config.middlewares.cors import setup_cors_middleware
from wstasks_backend.core.router import setup_router
from wstasks_backend.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

setup_cors_middleware(app)

setup_router(app)


if __name__ == "__main__":
    uvicorn.run("wstasks_backend.main:app", host="127.0.0.1", port=8000)
