"""empty message

Revision ID: 3f7381ec9a95
Revises: 8a63d9749521
Create Date: 2022-08-12 14:14:43.924620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f7381ec9a95'
down_revision = '8a63d9749521'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
