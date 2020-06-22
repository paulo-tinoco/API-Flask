"""product charge 001

Revision ID: 475b9482f47c
Revises: 45c47e52416a
Create Date: 2020-06-22 12:43:48.353201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475b9482f47c'
down_revision = '45c47e52416a'
branch_labels = None
depends_on = None


def upgrade():
    # Define table
    products = sa.sql.table("products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("price", sa.Float, unique=False, nullable=False),
        sa.Column("quantity", sa.Integer, unique=False, nullable=False),
        sa.Column("status", sa.Boolean, nullable=False, default=1)
    )

    # Add core products
    op.bulk_insert(products,
        [
            {"id": 1, "name": "Product 01", "price": 1.99, "quantity": 55},
            {"id": 2, "name": "Product 02", "price": 15.00, "quantity": 45},
            {"id": 3, "name": "Product 03", "price": 1.71, "quantity": 50},
            {"id": 4, "name": "Product 04", "price": 2.99, "quantity": 99},
        ]
    )

    categories = sa.sql.table("categories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("product_id", sa.Float, unique=False, nullable=False),
        sa.Column("status", sa.Boolean, nullable=False, default=1)
    )

    # Add core products
    op.bulk_insert(categories,
        [
            {"id": 1, "name": "Category 01", "product_id": 1},
            {"id": 2, "name": "Category 02", "product_id": 2},
            {"id": 3, "name": "Category 03", "product_id": 1},
        ]
    )

def downgrade():
    pass
