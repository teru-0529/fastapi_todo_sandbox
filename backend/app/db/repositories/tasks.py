#!/usr/bin/python3
# tasks.py

from app.db.repositories.base import BaseRepository
from app.models.tasks import TaskCreate, TaskInDB

import logging

logger = logging.getLogger(__name__)


CREATE_TASKS = """
  INSERT INTO todo.tasks (title, description, asaignee_id, is_significant, deadline)
  VALUES (:title, :description, :asaignee_id, :is_significant, :deadline)
  RETURNING id, title, description, asaignee_id, status, is_significant, deadline;
"""


class TaskRepository(BaseRepository):
    async def create(self, *, new_task: TaskCreate) -> TaskInDB:
        query_params = new_task.dict()
        task = await self.db.fetch_one(query=CREATE_TASKS, values=query_params)

        return TaskInDB(**task)
