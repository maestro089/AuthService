"""init

Revision ID: 2c1a39801d67
Revises: c5468db47141
Create Date: 2025-08-07 22:29:05.015425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c1a39801d67'
down_revision: Union[str, Sequence[str], None] = 'c5468db47141'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
