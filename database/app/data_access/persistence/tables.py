import sqlalchemy as sa

metadata = sa.MetaData()


secrets_table = sa.Table(
    "secrets",
    metadata,
    sa.Column("secret_id", sa.BigInteger, primary_key=True),
    sa.Column("name", sa.String(length=512), nullable=False, unique=True),
    sa.Column("value", sa.String(length=512), nullable=False),
    sa.Column("iv", sa.String(length=512), nullable=False),
    sa.Column("created_at", sa.DateTime, nullable=False),
)
