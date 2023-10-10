import logging
import os
import random
from datetime import datetime

import aiopg.sa

from db.models import *


async def init_pg():
    logging.info('Opening pg pool')
    conf = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT')),
        'database': os.getenv('DB_NAME'),
        'minsize': int(os.getenv('DB_POOL_MINSIZE')),
        'maxsize': int(os.getenv('DB_POOL_MAXSIZE'))
    }
    return await aiopg.sa.create_engine(**conf)


async def close_pg(engine):
    logging.warning('Closing pg...')
    if not engine:
        return
    engine.close()
    await engine.wait_closed()


async def db_healthcheck(conn):
    res = await conn.execute('SELECT 1 + 2')
    three = (await res.fetchone())[0]
    logging.info(f'PG IS HEALTH, 1 + 2 is {three}')


async def check_start(conn):
    res = await conn.execute(game_state.select())
    return (await res.fetchone())['started']


async def create_team(conn, name):
    while True:
        code = f'{random.randrange(1, 10 ** 6):06}'
        check = await conn.execute(
            team.select().where(team.c.connect_code == code)
        )
        res = await check.first()
        if not res:
            break
    await conn.execute(team.insert().values(connect_code=code, name=name))
    return code


async def create_user(conn, tg_id, username, full_name):
    await conn.execute(user.insert().values(tg_id=tg_id, username=username, full_name=full_name))


async def check_code(conn, team_code):
    check = await conn.execute(
        team.select().where(team.c.connect_code == team_code)
    )
    res = await check.first()
    if res:
        return True
    return False


async def connect_user(conn, tg_id, team_code):
    stmt = """
    UPDATE "user" SET team_fk = (SELECT id FROM team WHERE connect_code = %s) WHERE tg_id = %s
    """
    await conn.execute(stmt, (team_code, tg_id))
    stmt = """
    SELECT name FROM team WHERE connect_code = %s 
    """
    res = await conn.execute(stmt, (team_code,))
    return (await res.fetchone())[0]


async def change_state(conn):
    await conn.execute(game_state.update().values(started=True, start_time=datetime.utcnow()))


async def set_team_path(conn, path):
    stmt = """
    SELECT id FROM team WHERE path IS NULL; 
    """
    res = await conn.execute(stmt)
    res = await res.first()
    if res:
        stmt = """
        UPDATE team SET path = %s WHERE id = %s
        """
        await conn.execute(stmt, (path, res[0]))


async def create_all_team_task(conn):
    stmt = """
    SELECT id FROM task
    """
    res = await conn.execute(stmt)
    task_ids = await res.fetchall()
    stmt = """
    SELECT id FROM team;
    """
    res = await conn.execute(stmt)
    team_ids = await res.fetchall()
    for task_id in task_ids:
        for team_id in team_ids:
            await conn.execute(team_task.insert().values(team_fk=team_id[0], task_fk=task_id[0]))


async def check_user_exist(conn, tg_id):
    check = await conn.execute(
        user.select().where(user.c.tg_id == tg_id)
    )
    res = await check.fetchone()
    if res:
        return True
    return False


async def check_user_team(conn, tg_id):
    check = await conn.execute(
        user.select().where(user.c.tg_id == tg_id)
    )
    res = await check.fetchone()
    return res[2]


async def db_delete_game(conn):
    stmt = """
    DELETE FROM team_task; UPDATE game_state SET started = FALSE, start_time = NULL; 
    UPDATE team SET path = NULL, is_finished = FALSE, finish_time = NULL;
    """
    await conn.execute(stmt)


async def freeze_game(conn):
    stmt = """
    UPDATE team SET finish_time = now() WHERE is_finished = FALSE; UPDATE team SET is_finished = TRUE
    """
    await conn.execute(stmt)


async def get_team_statuses(conn):
    stmt = """
    SELECT is_finished FROM team;
    """
    res = await conn.execute(stmt)
    res = await res.fetchall()
    return [x[0] for x in res]


async def check_and_submit(conn, tg_id, answer):
    stmt = """
    SELECT answer FROM task
    INNER JOIN team_task tt on task.id = tt.task_fk
    INNER JOIN team t on tt.team_fk = t.id
    INNER JOIN "user" u on t.id = u.team_fk
    WHERE tt.is_current = TRUE AND u.tg_id = %s;
    """
    res = await conn.execute(stmt, (tg_id,))
    true_answer = (await res.fetchone())[0]
    if answer != true_answer:
        return False

    stmt = """
    UPDATE team_task SET is_current = FALSE, is_finished = TRUE
    WHERE is_current = TRUE AND team_fk = (
        SELECT t.id 
        FROM team t 
        INNER JOIN "user" u ON t.id = u.team_fk
        WHERE tg_id = %s
    )
    """

    await conn.execute(stmt, (tg_id,))

    return True


async def team_next_task(conn, tg_id):
    stmt = """
    SELECT path, team.id FROM team
    INNER JOIN "user" u on team.id = u.team_fk
    WHERE tg_id = %s
    """
    res = await conn.execute(stmt, (tg_id,))
    res = await res.fetchone()
    path = res[0]
    team_id = res[1]
    path = [int(x) for x in path.split(',')]
    path.pop(0)
    if len(path) == 0:
        stmt = """
        UPDATE team SET is_finished = TRUE, finish_time = (now() at time zone 'utc')
        WHERE id = %s
        """
        await conn.execute(stmt, (team_id,))
        return
    next_task = path[0]
    path = ','.join([str(y) for y in path])

    stmt = """
    UPDATE team SET path = %s WHERE id = %s;
    UPDATE team_task SET is_current = TRUE WHERE team_fk = %s AND task_fk = (SELECT id FROM task WHERE task_num = %s)
    """
    await conn.execute(stmt, (path, team_id, team_id, next_task))


async def get_curr_task_text(conn, tg_id):
    stmt = """
    SELECT 
    """


async def set_first_task(conn):
    stmt = """
    UPDATE team_task SET is_current = TRUE WHERE task_fk = (SELECT id FROM task WHERE task_num = 0);
    """
    await conn.execute(stmt)


async def get_tg_ids(conn, team_id):
    stmt = """
    SELECT tg_id FROM "user" WHERE team_fk = %s
    """
    res = await conn.execute(stmt, (team_id,))
    res = await res.fetchall()
    if len(res):
        return [r[0] for r in res]
    else:
        return []


async def get_finish_ids(conn):
    stmt = """
    SELECT id FROM team WHERE is_finished = TRUE AND is_sent = FALSE
    """
    res = await conn.execute(stmt)
    res = await res.fetchall()
    if len(res):
        tg_ids = []

        for r in res:
            stmt = """
            UPDATE team SET is_sent = TRUE WHERE id = %s
            """
            await conn.execute(stmt, (r[0],))
            tg_ids.extend(await get_tg_ids(conn, r[0]))
        return tg_ids
    return []


async def check_if_not_finished_by_user(conn, tg_id):
    stmt = """
    SELECT is_finished FROM team INNER JOIN "user" u on team.id = u.team_fk WHERE u.tg_id = %s
    """
    res = await conn.execute(stmt, (tg_id,))
    res = (await res.fetchone())[0]
    return res


async def get_all_teammates_tgs(conn, tg_id):
    stmt = """
    SELECT tg_id FROM "user" WHERE team_fk = 
    (SELECT team.id FROM team INNER JOIN "user" u ON team.id = u.team_fk WHERE u.tg_id = %s);
    """
    res = await conn.execute(stmt, (tg_id,))
    res = await res.fetchall()
    return [r[0] for r in res]


async def update_user_msg_id(conn, tg_id, msg_id):
    stmt = """
    UPDATE "user" SET last_msg_id = %s WHERE tg_id = %s
    """
    await conn.execute(stmt, (msg_id, tg_id))


async def get_team_current(conn, tg_id):
    stmt = """
    SELECT task.name FROM task
    INNER JOIN team_task tt on task.id = tt.task_fk
    INNER JOIN team t on tt.team_fk = t.id
    INNER JOIN "user" u on t.id = u.team_fk
    WHERE tt.is_current = TRUE AND u.tg_id = %s
    """
    res = await conn.execute(stmt, (tg_id,))
    res = await res.fetchone()
    return res[0]


async def get_all_tg_ids(conn):
    stmt = """
    SELECT tg_id FROM "user"
    """
    res = await conn.execute(stmt)
    return [r[0] for r in (await res.fetchall())]


async def get_first_task(conn):
    stmt = """
    SELECT name FROM task WHERE task_num = 0
    """
    res = await conn.execute(stmt)
    res = await res.fetchone()
    return res[0]


async def get_teams_current_tasks(conn):
    stmt = """
    UPDATE team_task SET auto_finish = auto_finish - 15 WHERE is_current = TRUE;
    SELECT tt.team_fk, tt.auto_finish, tt.is_loc_sent, name, location, description, last_msg FROM task
    INNER JOIN team_task tt on task.id = tt.task_fk
    WHERE tt.is_current = TRUE;
    """
    res = await conn.execute(stmt)
    return await res.fetchall()


async def sent_loc_to_team(conn, team_id):
    stmt = """
    UPDATE team_task SET is_loc_sent = TRUE WHERE team_fk = %s AND is_current = TRUE
    """
    await conn.execute(stmt, (team_id,))


async def get_teams_msg_ids(conn, team_id):
    stmt = """
    SELECT tg_id, last_msg_id FROM "user" INNER JOIN team t on "user".team_fk = t.id WHERE t.id = %s
    """
    res = await conn.execute(stmt, (team_id,))
    return await res.fetchall()


async def get_team_time_and_name(conn, tg_id):
    stmt = """
    SELECT name, finish_time - (SELECT start_time FROM game_state), team.id FROM team 
    INNER JOIN "user" u on team.id = u.team_fk 
    WHERE u.tg_id =  %s;
    """
    res = await conn.execute(stmt, (tg_id,))
    res = await res.fetchone()
    return res


async def get_team_with_members(conn):
    stmt = """
    SELECT name, id FROM team
    """
    res = await conn.execute(stmt)
    res = await res.fetchall()
    result = []
    for r in res:
        stmt = """
        SELECT username, full_name, tg_id FROM "user" WHERE team_fk = %s
        """
        ress = await conn.execute(stmt, (r[1],))
        ress = await ress.fetchall()
        result.append((r[0], ress))
    return result


async def get_teammates_by_team_id(conn, team_id):
    stmt = """
    SELECT username, full_name FROM "user" WHERE team_fk = %s
    """
    res = await conn.execute(stmt, (team_id,))
    return await res.fetchall()
