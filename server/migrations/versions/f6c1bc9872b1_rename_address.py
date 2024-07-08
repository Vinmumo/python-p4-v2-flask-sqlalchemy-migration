"""rename address

Revision ID: f6c1bc9872b1
Revises: 6ab383ac1ba9
Create Date: 2024-06-26 15:41:10.933290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c1bc9872b1'
down_revision = '6ab383ac1ba9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
