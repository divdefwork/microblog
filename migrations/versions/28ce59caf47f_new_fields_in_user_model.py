"""new fields in user model

Revision ID: 28ce59caf47f
Revises: 33e5f03e08f5
Create Date: 2020-09-18 20:23:32.740260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28ce59caf47f'
down_revision = '33e5f03e08f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###