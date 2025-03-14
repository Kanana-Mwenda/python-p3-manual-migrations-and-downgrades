"""rename name column to first_name

Revision ID: ac83dcee9c03
Revises: 791279dd0760
Create Date: 2025-03-10 08:28:00.288396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac83dcee9c03'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('students','first_name',new_column_name='email')
