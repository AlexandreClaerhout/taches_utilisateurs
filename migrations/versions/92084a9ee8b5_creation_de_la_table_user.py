"""Creation de la table User

Revision ID: 92084a9ee8b5
Revises: 
Create Date: 2025-05-22 00:47:53.327165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, TEXT


# revision identifiers, used by Alembic.
revision: str = '92084a9ee8b5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'user',
        Column("id", INTEGER, primary_key=True),
        Column('username', VARCHAR(50), nullable=False),
        Column('email', VARCHAR(100), nullable=False),
        Column('password', TEXT, nullable=False),
        Column('is_active', BOOLEAN, default=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user')
