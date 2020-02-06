"""empty message

Revision ID: 0e67a23612df
Revises: cb8e7828f2be
Create Date: 2020-01-28 01:07:58.315668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e67a23612df'
down_revision = 'cb8e7828f2be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidate',
    sa.Column('phone', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('linkedin', sa.Text(), nullable=False),
    sa.Column('exp_years', sa.Text(), nullable=False),
    sa.Column('duration', sa.Text(), nullable=False),
    sa.Column('summary', sa.Text(), nullable=False),
    sa.Column('skills', sa.Text(), nullable=False),
    sa.Column('experience', sa.Text(), nullable=False),
    sa.Column('education', sa.Text(), nullable=False),
    sa.Column('extra', sa.Text(), nullable=False),
    sa.Column('awards', sa.Text(), nullable=False),
    sa.Column('resume', sa.String(length=500), nullable=False),
    sa.Column('filename', sa.Text(), nullable=False),
    sa.Column('complete_resume', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('resume')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candidate')
    # ### end Alembic commands ###
