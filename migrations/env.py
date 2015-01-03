#flake8: noqa

from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

"""
ALEMBIC APPLICATION BOOSTRAPPING
------------------------------------------------------------------------------
Thers probably a better way to handle this but this has worked great for me so
far.  We instantiate out application using our factory passing in the desired
environement pulled from the alembic config section.  This is specified on the
command line using the -n NAME flag.

This allows us to neatly tie all of out database configuration state into one object.
As the pattern defined in this template is to pull all your models into your views the
application factory will ensure all the modls are picked up by alembic Thus ensuring that
autogenerate will find any changes you have made for you.

"""

from {{ PROJECT_NAME }}.app import create_app
from {{PROJECT_NAME}}.models import db

app = create_app()

target_metadata = db.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = app.config['SQLALCHEMY_DATABASE_URI']
    context.configure(url=url)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    alembic_config = config.get_section(config.config_ini_section)
    alembic_config['sqlalchemy.url'] = app.config['SQLALCHEMY_DATABASE_URI']
    engine = engine_from_config(
                alembic_config,
                prefix='sqlalchemy.',
                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
                connection=connection,
                target_metadata=target_metadata
                )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
