from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.celery import make_celery
from router import router
from lifespan import lifespan


app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

celery = make_celery()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
