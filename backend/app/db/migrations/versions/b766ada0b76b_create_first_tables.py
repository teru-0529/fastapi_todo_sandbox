"""create_schema

Revision ID: b766ada0b76b
Revises:
Create Date: 2022-10-24 21:40:51.026431

"""
from alembic import op

# import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b766ada0b76b"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
        CREATE FUNCTION set_modified_at() RETURNS TRIGGER AS $$
        BEGIN
            NEW.modified_at := now() AT TIME ZONE 'Asia/Tokyo';
            return NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )


def upgrade() -> None:
    op.execute("CREATE SCHEMA todo;")
    create_updated_at_trigger()


def downgrade() -> None:
    op.execute("DROP FUNCTION set_modified_at;")
    op.execute("DROP SCHEMA todo;")
