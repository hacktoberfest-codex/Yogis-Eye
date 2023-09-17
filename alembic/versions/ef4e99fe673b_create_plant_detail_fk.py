"""create plant detail FK

Revision ID: ef4e99fe673b
Revises: 9e71fc8922b6
Create Date: 2023-09-16 03:28:17.962254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef4e99fe673b'
down_revision: Union[str, None] = '9e71fc8922b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('details', sa.Column('plant_id', sa.Integer()))
    op.create_foreign_key('plant_detail_fk', source_table="details", referent_table="plants", local_cols=[
                          'plant_id'], remote_cols=['id'])


def downgrade() -> None:
    op.drop_constraint('plant_detail_fk', table_name="details")
    op.drop_column('details', 'plant_id')
