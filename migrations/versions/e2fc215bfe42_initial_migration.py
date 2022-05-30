"""Initial migration

Revision ID: e2fc215bfe42
Revises: 
Create Date: 2022-05-27 21:13:25.312744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2fc215bfe42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('dob', sa.String(length=20), nullable=False),
    sa.Column('minority', sa.String(length=20), nullable=False),
    sa.Column('caste', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('income', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
