import os

import peewee as pw

from wstasks_backend.config.settings import DATABASE_URL


db = pw.PostgresqlDatabase(
    DATABASE_URL
)


if not db.connect():
    raise Exception("Failed to connect to database")


class BaseModel(pw.Model):
    class Meta:
        database = db


class Task(BaseModel):
    id = pw.UUIDField(primary_key=True)
    name = pw.CharField()
    status = pw.CharField()
    created_at = pw.DateTimeField(constraints=[pw.SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_at = pw.DateTimeField(constraints=[pw.SQL("DEFAULT CURRENT_TIMESTAMP")])


if not db.table_exists("task"):  # type: ignore
    db.create_tables([Task])  # type: ignore
