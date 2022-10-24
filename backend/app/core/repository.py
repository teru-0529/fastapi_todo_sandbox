#!/usr/bin/python3
# repository.py

from typing import Callable

from app.db.repository import close_db_connection, connect_to_db
from fastapi import FastAPI


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
