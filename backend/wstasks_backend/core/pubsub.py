import asyncio
import json

from wstasks_backend.config.redis import redis
from wstasks_backend.ws_connections import WebSocketConnectionsSingleton


async def notify_ws_clients() -> None:
    pubsub = redis.pubsub()
    pubsub.subscribe("tasks_notifications")
    
    while True:
        message = pubsub.get_message(ignore_subscribe_messages=True)
        if message:
            for ws in WebSocketConnectionsSingleton.all():
                await ws.send_json(json.loads(message["data"]))
        
        await asyncio.sleep(0.1)
