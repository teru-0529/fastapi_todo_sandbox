"""create_schema

Revision ID: 3af1070341c5
Revises:
Create Date: 2022-10-25 14:08:59.952341

"""
from alembic import op

# import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3af1070341c5"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
        CREATE FUNCTION set_modified_at() RETURNS TRIGGER AS $$
        BEGIN
            NEW.modified_at := now();
            return NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )


def upgrade() -> None:
    op.execute("SET SESSION timezone TO 'Asia/Tokyo';")
    op.execute("CREATE SCHEMA todo;")
    create_updated_at_trigger()


def downgrade() -> None:
    op.execute("DROP FUNCTION set_modified_at;")
    op.execute("DROP SCHEMA todo;")
