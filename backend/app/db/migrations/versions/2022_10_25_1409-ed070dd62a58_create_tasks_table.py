"""create_tasks_table

Revision ID: ed070dd62a58
Revises: 3af1070341c5
Create Date: 2022-10-25 14:09:11.820940

"""
from typing import Tuple
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ed070dd62a58"
down_revision = "3af1070341c5"
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
            comment="登録日時",
        ),
        sa.Column(
            "modified_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
            comment="更新日時",
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
        sa.Column(
            "is_significant",
            sa.Boolean,
            nullable=False,
            server_default="False",
            comment="重要タスク",
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
