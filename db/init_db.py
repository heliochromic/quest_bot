import os

from sqlalchemy import create_engine, MetaData

from db.models import *
from db.sample_data import *

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_CONFIG = {
    'user': os.getenv('ADMIN_DB_USER'),
    'password': os.getenv('ADMIN_DB_PASS'),
    'host': os.getenv('ADMIN_DB_HOST'),
    'port': int(os.getenv('ADMIN_DB_PORT')),
    'database': os.getenv('ADMIN_DB_NAME')
}

ADMIN_DB_URL = DSN.format(**ADMIN_CONFIG)

admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')

USER_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DB_NAME')
}

USER_DB_URL = DSN.format(**USER_CONFIG)
user_engine = create_engine(USER_DB_URL)


def setup_db(config):
    db_name = config['database']
    db_user = config['user']
    db_pass = config['password']

    conn = admin_engine.connect()
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.execute("CREATE USER %s WITH PASSWORD '%s'" % (db_user, db_pass))
    conn.execute("CREATE DATABASE %s ENCODING 'UTF8'" % db_name)
    conn.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s" %
                 (db_name, db_user))
    conn.close()


def teardown_db(config):
    db_name = config['database']
    db_user = config['user']

    conn = admin_engine.connect()
    conn.execute("""
      SELECT pg_terminate_backend(pg_stat_activity.pid)
      FROM pg_stat_activity
      WHERE pg_stat_activity.datname = '%s'
        AND pid <> pg_backend_pid();""" % db_name)
    conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
    conn.execute("DROP ROLE IF EXISTS %s" % db_user)
    conn.close()


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine,
                    tables=[team, task, user, team_task, game_state])


def drop_tables(engine):
    meta = MetaData()
    meta.drop_all(bind=engine,
                  tables=[team, task, user, team_task, game_state])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(game_state.insert(), [
        {'started': False}
    ])
    if os.getenv('MODE') == 'Production':
        conn.execute(task.insert(), get_prod_tasks())
    elif os.getenv('MODE') == 'Testing':
        conn.execute(task.insert(), get_test_tasks())
    else:
        conn.execute(task.insert(), get_tasks())
    conn.close()


def init_db():
    setup_db(USER_CONFIG)
    drop_tables(engine=user_engine)

    create_tables(engine=user_engine)
    sample_data(engine=user_engine)
    # teardown_db(config)


if __name__ == '__main__':
    init_db()
