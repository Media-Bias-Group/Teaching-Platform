"""empty message

Revision ID: ec9724f485d5
Revises: 91bb015d3566
Create Date: 2020-07-10 20:09:58.380378

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec9724f485d5'
down_revision = '91bb015d3566'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('survey_groups_ibfk_1', 'survey_groups', type_='foreignkey')
    op.drop_column('survey_groups', 'survey_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_groups', sa.Column('survey_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('survey_groups_ibfk_1', 'survey_groups', 'surveys', ['survey_id'], ['id'])
    # ### end Alembic commands ###