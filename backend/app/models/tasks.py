#!/usr/bin/python3
# tasks.py

from datetime import date
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
    is_significant: Optional[bool]
    deadline: Optional[date]


class TaskCreate(CoreModel):
    title: str
    description: Optional[str]
    asaignee_id: Optional[str]
    is_significant: bool = False
    deadline: Optional[date]

    class Config:
        schema_extra = {
            "example": {
                "title": "create db model",
                "description": "データベースモデルを作成する。",
                "asaignee_id": "000",
                "is_significant": False,
                "deadline": "2022-10-27",
            }
        }


class TaskUpdate(TaskBase):
    desctiption: str
    asaignee_id: str
    status: TaskStatus


class TaskInDB(IDModelMixin, TaskBase):
    title: str
    status: TaskStatus
    is_significant: bool


class TaskPublic(IDModelMixin, TaskBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "create db model",
                "description": "データベースモデルを作成する。",
                "asaignee_id": "000",
                "status": "TODO",
                "is_significant": False,
                "deadline": "2022-10-27",
            }
        }
