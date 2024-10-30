from fastapi import WebSocket


class WebSocketConnectionsSingleton:
    _connections: set[WebSocket] = set()

    @classmethod
    def add(cls, ws: WebSocket) -> None:
        cls._connections.add(ws)

    @classmethod
    def remove(cls, ws: WebSocket) -> None:
        cls._connections.remove(ws)

    @classmethod
    def count(cls) -> int:
        return len(cls._connections)

    @classmethod
    def all(cls) -> set[WebSocket]:
        return cls._connections.copy()
