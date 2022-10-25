"""create_tasks_table

Revision ID: 34a655057c89
Revises: b766ada0b76b
Create Date: 2022-10-25 12:32:30.748593

"""
from typing import Tuple
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "34a655057c89"
down_revision = "b766ada0b76b"
branch_labels = None
depends_on = None


def timestamps(indexed: bool = False) -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
        sa.Column(
            "modified_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
    )


def create_tasks_table() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, primary_key=True, comment="タスクID"),
        sa.Column("title", sa.String(30), nullable=False, comment="タイトル"),
        sa.Column("description", sa.Text, nullable=True, comment="内容"),
        sa.Column("asaignee_id", sa.String(3), nullable=True, comment="担当者ID"),
        sa.Column(
            "status",
            sa.Enum("TODO", "DOING", "DONE", name="status"),
            nullable=False,
            server_default="TODO",
            index=True,
            comment="タスクステータス",
        ),
        *timestamps(),
        schema="todo",
    )
    op.execute(
        """
        CREATE TRIGGER tasks_modified
            BEFORE UPDATE
            ON todo.tasks
            FOR EACH ROW
        EXECUTE PROCEDURE set_modified_at();
        """
    )


def upgrade() -> None:
    create_tasks_table()


def downgrade() -> None:
    op.drop_table("tasks", schema="todo")
    op.execute("DROP TYPE status;")
