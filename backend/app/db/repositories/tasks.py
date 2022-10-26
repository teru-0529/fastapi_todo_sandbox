#!/usr/bin/python3
# tasks.py

from app.db.repositories.base import BaseRepository
from app.models.tasks import TaskCreate, TaskInDB

CREATE_TASKS = """
  INSERT INTO todo.tasks (title, description, asaignee_id)
  VALUES (:title, :description, :asaignee_id)
  RETURNING id, title, description, asaignee_id, status;
"""


class TaskRepository(BaseRepository):
    async def create(self, *, new_task: TaskCreate) -> TaskInDB:
        query_params = new_task.dict()
        task = await self.db.fetch_one(query=CREATE_TASKS, values=query_params)

        return TaskInDB(**task)
