#!/usr/bin/python3
# tasks.py

from typing import List

from app.api.dependencies.database import get_repository
from app.db.repositories.tasks import TaskRepository
from app.models.tasks import TaskCreate, TaskPublic
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

router = APIRouter()


@router.get("/")
async def get_all_hedgehogs() -> List[dict]:
    hedgehogs = [
        {"id": 1, "name": "momo", "color": "SALT & PEPPER", "age": 2},
        {"id": 2, "name": "coco", "color": "DARK GRAY", "age": 1.5},
    ]
    return hedgehogs


@router.post(
    "/",
    response_model=TaskPublic,
    name="tasks:create",
    response_description="Created new Task",
    status_code=HTTP_201_CREATED,
)
async def create_task(
    new_task: TaskCreate = Body(...),
    task_repo: TaskRepository = Depends(get_repository(TaskRepository)),
) -> TaskPublic:
    """
    タスクの新規作成。**id**は自動採番され、**status**は`TODO`が登録される。:

    - **title**: タスクの名称[Reqired]
    - **description**: タスクの詳細内容
    - **asaignee_id**: タスクの担当者
    - **is_significant**: 重要タスクの場合にTrue[Default=False]
    - **deadline**: タスク期限日(YYYY-MM-DD) ※当日以降の日付を指定可能
    """
    task = await task_repo.create(new_task=new_task)
    return task
