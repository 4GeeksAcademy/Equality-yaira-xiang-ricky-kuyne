"""empty message

Revision ID: 9e483caf7910
Revises: a644cfa01742
Create Date: 2023-08-12 20:49:00.829387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e483caf7910'
down_revision = 'a644cfa01742'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(length=50), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('img', sa.String(length=255), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_expired', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['buyer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=True))
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('shopname', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('reviews', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('address', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('pictures', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('transactions', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('favorites', sa.Boolean(), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('favorites')
        batch_op.drop_column('transactions')
        batch_op.drop_column('pictures')
        batch_op.drop_column('address')
        batch_op.drop_column('reviews')
        batch_op.drop_column('shopname')
        batch_op.drop_column('name')
        batch_op.drop_column('username')

    op.drop_table('product')
    # ### end Alembic commands ###