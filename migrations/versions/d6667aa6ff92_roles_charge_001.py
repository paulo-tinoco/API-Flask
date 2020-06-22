"""roles charge 001

Revision ID: d6667aa6ff92
Revises: 071c848d6d66
Create Date: 2020-06-20 09:44:32.179890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6667aa6ff92'
down_revision = '071c848d6d66'
branch_labels = None
depends_on = None


def upgrade():
    # Define table
    roles = sa.sql.table("roles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("status", sa.Boolean, nullable=False, default=1)
    )

    # Add core roles
    op.bulk_insert(roles,
        [
            {"id": 1, "name": "Administrator"},
            {"id": 2, "name": "Visitor"},
        ]
    ) 


def downgrade():
    pass
