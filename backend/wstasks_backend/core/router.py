import json
import random
from typing import Any

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.routing import APIRouter

from wstasks_backend.config.database import Task as DBTask
from wstasks_backend.config.redis import redis
from wstasks_backend.core.serializers import TasksListResponse
from wstasks_backend.core.tasks import generic_task
from wstasks_backend.ws_connections import WebSocketConnectionsSingleton


def setup_router(app: FastAPI) -> None:
    router = APIRouter()

    @router.get("/", response_model=TasksListResponse)
    def index(page: int = 1, page_size: int = 20) -> dict[str, Any]:
        limit = page_size
        offset = (page - 1) * page_size

        tasks = (
            DBTask.select().order_by(DBTask.updated_at.desc()).limit(limit).offset(offset)
        )
        
        count = DBTask.select().count()
        total_pages = count // page_size + 1
        
        return {"tasks": tasks, "total_items": count, "total_pages": total_pages}

    @router.post("/create-task")
    def create_task() -> dict[str, Any]:
        duration = random.uniform(10, 60)

        result = generic_task.delay(duration)  # type: ignore

        DBTask.create(id=result.id, name=generic_task.name, status=result.status)

        message = {"task_id": result.id, "status": result.status}
        redis.publish("tasks_notifications", json.dumps(message))

        return {"task": result.id}

    @router.websocket("/ws/tasks")
    async def ws_tasks(ws: WebSocket) -> None:
        await ws.accept()
        WebSocketConnectionsSingleton.add(ws)

        try:
            while ws.client_state.value < 3:
                data = await ws.receive_json()
                
                task_id = data["task_id"]
                task = DBTask.get(DBTask.id == task_id)
                
                await ws.send_json(task.__data__)
        except WebSocketDisconnect:
            WebSocketConnectionsSingleton.remove(ws)
    
    
    app.include_router(router)
