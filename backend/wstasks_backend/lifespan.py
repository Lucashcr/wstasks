import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from wstasks_backend.pubsub import notify_ws_clients


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(notify_ws_clients())
    yield
    task.cancel()
