#!/usr/bin/python3
# tasks.py

import logging

from app.api.schemas.tasks import TaskCreate, TaskInDB
from app.db.models import Task, printTaskList
from app.db.repositories.base import BaseRepository

logger = logging.getLogger(__name__)

# FIXME:
CREATE_TASKS = """
  INSERT INTO todo.tasks (title, description, asaignee_id, is_significant, deadline)
  VALUES (:title, :description, :asaignee_id, :is_significant, :deadline)
  RETURNING id, title, description, asaignee_id, status, is_significant, deadline;
"""


class TaskRepository(BaseRepository):
    async def create(self, *, new_task: TaskCreate) -> TaskInDB:
        printTaskList()  # FIXME:
        query_params = new_task.dict()
        task = await self.db.fetch_one(query=CREATE_TASKS, values=query_params)

        return TaskInDB(**task)
