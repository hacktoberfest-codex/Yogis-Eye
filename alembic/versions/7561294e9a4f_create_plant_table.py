"""create plant table

Revision ID: 7561294e9a4f
Revises: 
Create Date: 2023-09-16 01:34:06.851474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7561294e9a4f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('plants', sa.Column('id', sa.Integer(
    ), nullable=False, primary_key=True, index=True, autoincrement=True),
                    sa.Column('plant_text', sa.String()))
    
    


def downgrade() -> None:
    op.drop_table('plants')