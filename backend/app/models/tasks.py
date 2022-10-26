#!/usr/bin/python3
# tasks.py

from enum import Enum
from typing import Optional

from app.models.core import CoreModel, IDModelMixin


class TaskStatus(str, Enum):
    todo = "TODO"
    doing = "DOING"
    done = "DONE"


class TaskBase(CoreModel):
    title: Optional[str]
    description: Optional[str]
    asaignee_id: Optional[str]
    status: Optional[TaskStatus]


class TaskCreate(CoreModel):
    title: str
    description: Optional[str]
    asaignee_id: Optional[str]


class TaskUpdate(TaskBase):
    desctiption: str
    asaignee_id: str
    status: TaskStatus


class TaskInDB(IDModelMixin, TaskBase):
    title: str
    status: TaskStatus


class TaskPublic(IDModelMixin, TaskBase):
    pass
