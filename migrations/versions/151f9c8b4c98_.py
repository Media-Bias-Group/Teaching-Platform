"""empty message

Revision ID: 151f9c8b4c98
Revises: 649015aba760
Create Date: 2020-07-13 20:26:24.457897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151f9c8b4c98'
down_revision = '649015aba760'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_pool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('survey_record_id', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['survey_record_id'], ['survey_record.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('survey_annotations', sa.Column('sentence_group_id', sa.String(length=150), nullable=True))
    op.create_foreign_key(None, 'survey_annotations', 'survey_groups', ['sentence_group_id'], ['id'])
    op.add_column('test_survey_annotations', sa.Column('sentence_group_id', sa.String(length=150), nullable=True))
    op.create_foreign_key(None, 'test_survey_annotations', 'test_survey_groups', ['sentence_group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'test_survey_annotations', type_='foreignkey')
    op.drop_column('test_survey_annotations', 'sentence_group_id')
    op.drop_constraint(None, 'survey_annotations', type_='foreignkey')
    op.drop_column('survey_annotations', 'sentence_group_id')
    op.drop_table('user_pool')
    # ### end Alembic commands ###
