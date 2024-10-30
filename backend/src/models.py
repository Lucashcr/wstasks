from datetime import datetime
from pydantic import BaseModel, Field
from pydantic.types import UUID4


class TaskModel(BaseModel):
    id: UUID4
    name: str
    status: str
    created_at: datetime = Field(serialization_alias="createdAt")
    updated_at: datetime = Field(serialization_alias="updatedAt")


class TasksListResponse(BaseModel):
    tasks: list[TaskModel]
    total_items: int = Field(serialization_alias="totalItems")
    total_pages: int = Field(serialization_alias="totalPages")
