import asyncio
import json
import logging
import os
import random

import db.db as db
from templates import msg_template

# paths = ['0,4,1,10,3,12,9,13,14', '0,2,8,11,5,7,6,13,14']
paths = ['0,1,2,3,4,5,6,7,8,9,10,11,12,13']
if os.getenv('MODE') == 'Production':
    paths = ['0,1,4,3,2,5,6,13', '0,10,3,4,11,12,7,13', '0,2,1,11,10,6,9,13', '0,4,5,10,3,8,7,13', '0,11,2,8,5,7,9,13',
             '0,5,9,6,12,8,1,13', '0,3,12,7,8,11,4,13', '0,9,6,12,2,11,1,13', '0,8,11,2,4,12,9,13', '0,1,9,3,8,5,12,13',
             '0,10,4,5,7,6,9,13', '0,6,7,1,9,2,3,13', '0,7,8,9,1,3,5,13', '0,12,10,3,6,1,2,13', '0,3,2,10,1,4,8,13']
if os.getenv('MODE') == 'Development':
    paths = ['0,1,2,3,4,5,6,7,8', '0,5,6,7,3,4,2,1,8', '0,6,1,2,3,4,5,7,8', '0,1,4,5,7,6,3,2,8']
db_engine = None
bot = None


async def prepare_game():
    random.shuffle(paths)
    async with db_engine.acquire() as conn:
        for x in paths:
            await db.set_team_path(conn, x)
        await db.create_all_team_task(conn)
        await db.set_first_task(conn)


async def change_game_state():
    async with db_engine.acquire() as conn:
        await db.change_state(conn)


async def game_process():
    while True:
        logging.info('Game process')
        async with db_engine.acquire() as conn:
            status = await db.check_start(conn)
            if not status:
                logging.info('Game finished!')
                return
            db_rows = await db.get_teams_current_tasks(conn)
            for row in db_rows:
                await process_team_task(row, conn)

            # tg_ids = await db.get_finish_ids(conn)
            # if len(tg_ids):
            #     await send_to(tg_ids, 'vitayu!')

        await asyncio.sleep(14)


async def start_game(db_en, bot_):
    global db_engine, bot
    db_engine = db_en
    bot = bot_

    async with db_engine.acquire() as conn:
        status = await db.check_start(conn)

        if not status:
            logging.info('Preparing game')
            await prepare_game()
            await change_game_state()
            tg_ids = await db.get_all_tg_ids(conn)
            first_task = await db.get_first_task(conn)
            msg = msg_template(first_task, 420, None, 1020, None, 1800, None)
            msg = {
                'type': 'text',
                'body': {
                    'text': msg,
                    'parse_mode': 'Markdown'
                }
            }
            await send_to(tg_ids, msg, conn)
    await game_process()


async def send_to(tg_ids, msg, conn, bot_instance=None):
    if bot_instance is None:
        bot_instance = bot
    for tg_id in tg_ids:
        if msg['type'] == 'text':
            msg_to_write = await bot_instance.send_message(tg_id, msg['body']['text'],
                                                           parse_mode=msg['body']['parse_mode'])
            await db.update_user_msg_id(conn, tg_id, msg_to_write.message_id)
        elif msg['type'] == 'location':
            await bot_instance.send_location(tg_id, msg['body']['latitude'], msg['body']['longitude'])
        elif msg['type'] == 'photo':
            print('send_photo')
        elif msg['type'] == 'audio':
            print('audio')


async def edit_message(tg_id, msg_id, msg, bot_instance=None, parse_mode='Markdown'):
    if bot_instance is None:
        bot_instance = bot
    await bot_instance.edit_message_text(msg, tg_id, msg_id, parse_mode=parse_mode)


async def process_team_task(db_row, conn):
    team_id = db_row[0]
    auto_finish = db_row[1]
    is_loc_sent = db_row[2]
    name = db_row[3]
    location = db_row[4]
    description = db_row[5]
    last_msg = db_row[6]

    if auto_finish < 0:
        return

    time_first = auto_finish - 1380
    if time_first <= 0:
        time_first = 0
    else:
        description = None
    teammates = await db.get_teams_msg_ids(conn, team_id)

    time_second = auto_finish - 780
    if time_second <= 0:
        time_second = 0
        if not is_loc_sent:
            await db.sent_loc_to_team(conn, team_id)
            await send_to([x[0] for x in teammates], json.loads(location), conn)
    else:
        location = None

    time_third = auto_finish
    if time_third <= 0:
        time_third = 0
    else:
        last_msg = None

    text = msg_template(name, time_first, description, time_second, location, time_third, last_msg)

    for teammate in teammates:
        tg_id = teammate[0]
        msg_id = teammate[1]
        await edit_message(tg_id, msg_id, text)
