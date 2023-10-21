import datetime

from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, ForeignKey, DateTime, BigInteger

__all__ = ['user', 'team', 'task', 'team_task', 'game_state']

meta = MetaData()

game_state = Table(
    'game_state', meta,

    Column('id', Integer, primary_key=True),
    Column('start_time', DateTime),
    Column('started', Boolean, nullable=False, default=False)
)

team = Table(
    'team', meta,

    Column('id', Integer, primary_key=True),
    Column('connect_code', String, nullable=False),
    Column('is_finished', Boolean, nullable=False, default=False),
    Column('is_sent', Boolean, nullable=False, default=False),
    Column('path', String),
    Column('name', String, nullable=False),
    Column('finish_time', DateTime)
)

task = Table(
    'task', meta,

    Column('id', Integer, primary_key=True),
    Column('task_num', Integer, nullable=False),
    Column('name', String),
    Column('location', String),
    Column('description', String),
    Column('answer', String),
    Column('last_msg', String),
    Column('need_to_approved', Boolean, nullable=False, default=False),
    Column('is_final', Boolean, nullable=False, default=False)
)

user = Table(
    'user', meta,

    Column('id', BigInteger, primary_key=True),
    Column('tg_id', BigInteger, nullable=False),
    Column('team_fk', Integer, ForeignKey('team.id', ondelete='RESTRICT', onupdate='CASCADE')),
    Column('last_msg_id', Integer, nullable=True),
    Column('username', String),
    Column('full_name', String)
)

team_task = Table(
    'team_task', meta,

    Column('team_fk', Integer, ForeignKey('team.id', ondelete='RESTRICT', onupdate='CASCADE')),
    Column('task_fk', Integer, ForeignKey('task.id', ondelete='RESTRICT', onupdate='CASCADE')),
    Column('is_finished', Boolean, nullable=False, default=False),
    Column('is_current', Boolean, nullable=False, default=False),
    Column('is_loc_sent', Boolean, nullable=False, default=False),
    Column('auto_finish', Integer, nullable=False, default=1200)
)
