"""empty message

Revision ID: 464019c50f84
Revises: 6499bcacf1ee
Create Date: 2022-06-09 15:30:20.896247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '464019c50f84'
down_revision = '6499bcacf1ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('solicitations', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('solicitations', sa.Column('responded_at', sa.DateTime(), nullable=True))
    op.add_column('solicitations', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('solicitations', 'updated_at')
    op.drop_column('solicitations', 'responded_at')
    op.drop_column('solicitations', 'created_at')
    # ### end Alembic commands ###
