from datetime import datetime
import json
import time

from celery import Task, shared_task
from celery.result import AsyncResult

from wstasks_backend.config.database import Task as DBTask
from wstasks_backend.config.redis import make_redis

class BaseTask(Task):
    def update_status_on_database(self, task_id) -> None:
        result = AsyncResult(task_id)
        current_time = datetime.now()
        DBTask.update(status=result.status, updated_at=current_time).where(
            DBTask.id == task_id
        ).execute()
    
    def notify_ws_clients(self, task_id, status) -> None:
        message = {"task_id": task_id, "status": status}
        redis = make_redis()
        redis.publish("tasks_notifications", json.dumps(message))

    def on_success(self, retval, task_id, args, kwargs):
        self.update_status_on_database(task_id)
        self.notify_ws_clients(task_id, "SUCCESS")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.update_status_on_database(task_id)
        self.notify_ws_clients(task_id, "FAILURE")


@shared_task(base=BaseTask)
def generic_task(duration: float) -> dict[str, float]:
    time.sleep(duration)
    return {"duration": duration}