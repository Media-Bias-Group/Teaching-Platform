"""empty message

Revision ID: 95b0ef44c928
Revises: 72059829a787
Create Date: 2020-07-13 20:57:30.018987

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '95b0ef44c928'
down_revision = '72059829a787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_pool', sa.Column('survey_rec_id', sa.String(length=150), nullable=False))
    op.drop_constraint('user_pool_ibfk_1', 'user_pool', type_='foreignkey')
    op.drop_column('user_pool', 'survey_record_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_pool', sa.Column('survey_record_id', mysql.VARCHAR(length=150), nullable=True))
    op.create_foreign_key('user_pool_ibfk_1', 'user_pool', 'survey_record', ['survey_record_id'], ['id'])
    op.drop_column('user_pool', 'survey_rec_id')
    # ### end Alembic commands ###