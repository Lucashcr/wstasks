import asyncio
import json

from config.redis import make_redis
from ws_connections import WebSocketConnectionsSingleton


async def notify_ws_clients() -> None:
    redis = make_redis()
    pubsub = redis.pubsub()
    pubsub.subscribe("tasks_notifications")
    
    while True:
        message = pubsub.get_message(ignore_subscribe_messages=True)
        if message:
            for ws in WebSocketConnectionsSingleton.all():
                await ws.send_json(json.loads(message["data"]))
        
        await asyncio.sleep(0.1)
