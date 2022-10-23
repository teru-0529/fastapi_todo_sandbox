#!/usr/bin/python3
# test.py

from app.api.routes.tasks import router as task_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(task_router, prefix="/tasks", tags=["tasks"])
