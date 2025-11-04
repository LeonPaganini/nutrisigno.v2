"""
Alembic environment script.

This file is executed by the Alembic migration tool to set up
migration context.  The skeleton does not include any migrations,
but this file is provided as a placeholder.  Real projects
should configure the SQLAlchemy engine and target metadata.
"""

from alembic import context
from sqlalchemy import engine_from_config, pool

from ..models.base import Base

# Add your model's MetaData object here for ``autogenerate`` support
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in offline mode.

    This configures the context with just a URL and not an Engine.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    context.configure(url="sqlite:///./nutrisigno.db", target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode.

    In this scenario we need to create an Engine and associate a
    connection with the context.
    """
    configuration = context.config
    connectable = engine_from_config(
        configuration.get_section(configuration.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()