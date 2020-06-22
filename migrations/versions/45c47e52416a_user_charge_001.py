"""user charge 001

Revision ID: 45c47e52416a
Revises: 0a8ac0742768
Create Date: 2020-06-22 11:15:04.830601

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision = '45c47e52416a'
down_revision = '0a8ac0742768'
branch_labels = None
depends_on = None


def upgrade():
    # Define table
    roles = sa.sql.table("users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, unique=False, nullable=False),
        sa.Column("email", sa.String, unique=True, nullable=False),
        sa.Column("password", sa.String, unique=False, nullable=False),
        sa.Column("role_id", sa.Integer, unique=False, nullable=False),
        sa.Column("status", sa.Boolean, nullable=False, default=1)
    )

    # Add core roles
    op.bulk_insert(roles,
        [
            {"id": 1, "name": "Administrator", "email": "admin@example.com" ,"password": generate_password_hash('123456'), "role_id": 1},
        ]
    ) 


def downgrade():
    pass
