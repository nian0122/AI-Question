"""empty message

Revision ID: ef39e2c246c7
Revises: 
Create Date: 2023-11-14 23:15:03.590255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef39e2c246c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ai_answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ai_question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('picture', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('picture', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.LargeBinary(),
               nullable=False)

    with op.batch_alter_table('tmc', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=100),
               comment=None,
               existing_comment='药名',
               existing_nullable=False)
        batch_op.alter_column('othername',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='别名')
        batch_op.alter_column('englishname',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='外语名')
        batch_op.alter_column('source',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='分布')
        batch_op.alter_column('produce',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='部位')
        batch_op.alter_column('shap',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='形状')
        batch_op.alter_column('stc',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='归经')
        batch_op.alter_column('effect',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='功效')
        batch_op.alter_column('application',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='应用')
        batch_op.alter_column('study',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='研究')
        batch_op.alter_column('composition',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='成分')
        batch_op.alter_column('taboo',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='禁忌')
        batch_op.alter_column('formula',
               existing_type=mysql.TEXT(),
               nullable=False,
               comment=None,
               existing_comment='配伍药方')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=100), nullable=False))
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_column('Username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Username', mysql.VARCHAR(length=64), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=False)
        batch_op.drop_column('username')

    with op.batch_alter_table('tmc', schema=None) as batch_op:
        batch_op.alter_column('formula',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='配伍药方')
        batch_op.alter_column('taboo',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='禁忌')
        batch_op.alter_column('composition',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='成分')
        batch_op.alter_column('study',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='研究')
        batch_op.alter_column('application',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='应用')
        batch_op.alter_column('effect',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='功效')
        batch_op.alter_column('stc',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='归经')
        batch_op.alter_column('shap',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='形状')
        batch_op.alter_column('produce',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='部位')
        batch_op.alter_column('source',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='分布')
        batch_op.alter_column('englishname',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='外语名')
        batch_op.alter_column('othername',
               existing_type=mysql.TEXT(),
               nullable=True,
               comment='别名')
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=100),
               comment='药名',
               existing_nullable=False)

    with op.batch_alter_table('picture', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=sa.LargeBinary(),
               type_=mysql.VARCHAR(length=100),
               nullable=True)

    op.drop_table('images')
    op.drop_table('ai_question')
    op.drop_table('ai_answer')
    # ### end Alembic commands ###
