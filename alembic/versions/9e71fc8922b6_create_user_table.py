"""create user table

Revision ID: 9e71fc8922b6
Revises: eb869a6ae727
Create Date: 2023-09-16 02:02:30.704279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e71fc8922b6'
down_revision: Union[str, None] = 'eb869a6ae727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False, primary_key=True, index=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True))


def downgrade() -> None:
    op.drop_table('users')
