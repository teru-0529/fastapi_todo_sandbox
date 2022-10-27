#!/usr/bin/python3
# tasks.py

from app.db.repositories.base import BaseRepository
from app.models.tasks import TaskCreate, TaskInDB

import logging

logger = logging.getLogger(__name__)


CREATE_TASKS = """
  INSERT INTO todo.tasks (title, description, asaignee_id, is_significant)
  VALUES (:title, :description, :asaignee_id, :is_significant)
  RETURNING id, title, description, asaignee_id, status, is_significant;
"""


class TaskRepository(BaseRepository):
    async def create(self, *, new_task: TaskCreate) -> TaskInDB:
        logger.warn("--- DATABASE CONNECTION ERROR ---")
        logger.warn(new_task)
        logger.warn("--- DATABASE CONNECTION ERROR ---")

        query_params = new_task.dict()
        task = await self.db.fetch_one(query=CREATE_TASKS, values=query_params)

        return TaskInDB(**task)
