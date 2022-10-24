#!/usr/bin/python3
# test.py

from app.api.routes.tasks import router as task_router
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    health_ok = {"health": "ok"}
    return health_ok


router.include_router(task_router, prefix="/tasks", tags=["tasks"])
