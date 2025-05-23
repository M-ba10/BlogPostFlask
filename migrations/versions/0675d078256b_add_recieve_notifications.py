"""add recieve_notifications

Revision ID: 0675d078256b
Revises: 
Create Date: 2025-04-29 18:33:35.112354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0675d078256b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('receive_notifications', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('receive_notifications')

    # ### end Alembic commands ###
