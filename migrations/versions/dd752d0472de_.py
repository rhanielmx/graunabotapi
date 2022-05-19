"""empty message

Revision ID: dd752d0472de
Revises: de22d740cbff
Create Date: 2022-05-19 01:16:25.847058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd752d0472de'
down_revision = 'de22d740cbff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'requestNumber')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('requestNumber', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###