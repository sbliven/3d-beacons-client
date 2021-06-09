"""empty message

Revision ID: b80709a3edef
Revises: 77615a2829d4
Create Date: 2021-03-03 14:39:50.381582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80709a3edef'
down_revision = '77615a2829d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model_chain_segment', 'uniprot_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('model_chain_segment', 'uniprot_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
