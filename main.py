import asyncio

from aiogram import Bot, Dispatcher, executor, types, filters

from db.db import *
from templates import msg_template, start_msg, grats_msg_template, final_msg_template, start_game_msg, \
    correct_answer_template, your_teammates
from utilities import set_up_logging, load_env

# bot token
API_TOKEN = "6389836959:AAFNKiSQ2UYNn222l4dva0lhhlTtFvhS-pU"

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    logging.warning('Cannot import uvloop, using asyncio event loop instead')

loop = asyncio.get_event_loop()

bot = Bot(token=API_TOKEN, loop=loop)
dp = Dispatcher(bot, loop=loop)
db_engine = None

IS_STARTED = False
# tg ids
MAIN_ADMIN = 5329272290
ADMINS = [5329272290, 377594478, 729696014, 131538276, 0]

APPROVE_CHAT = 0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if IS_STARTED:
        await bot.send_message(message.chat.id,
                               'А ти розумник, твій код: C321')
    else:
        msg = start_msg()
        await bot.send_message(message.chat.id, msg['body']['text'], parse_mode=msg['body']['parse_mode'])


@dp.message_handler(commands=['add_team'])
async def add_team(message: types.Message):
    if not IS_STARTED:
        if message.from_user.id in ADMINS:
            team_name = message.get_args()
            async with db_engine.acquire() as conn:
                code = await create_team(conn, team_name)
            await bot.send_message(message.chat.id,
                                   f'Нову команду {team_name} зареєстровано! Код, щоб долучитися: {code}')


@dp.message_handler(commands=['connect'])
async def connect_to_team(message: types.Message):
    if not IS_STARTED:
        team_code = message.get_args()
        async with db_engine.acquire() as conn:
            if not await check_user_exist(conn, message.from_user.id):
                await create_user(conn, message.from_user.id, message.from_user.username, message.from_user.full_name)
            if await check_user_team(conn, message.from_user.id):
                await bot.send_message(message.chat.id, 'Ти вже долучився до команди')
                return
            check = await check_code(conn, team_code)
            if not check:
                await bot.send_message(message.chat.id, f'Упс, щось не так з цим кодом: {team_code}')
            else:
                team_name = await connect_user(conn, message.from_user.id, team_code)
                await bot.send_message(message.chat.id, f'Вітаємо, ти в группі: {team_name}')


@dp.message_handler(commands=['pg_healthcheck'])
async def pg_healthcheck(message: types.Message):
    try:
        async with db_engine.acquire() as conn:
            await db_healthcheck(conn)
        await bot.send_message(message.chat.id, 'Pg is health')
    except Exception:
        await bot.send_message(message.chat.id, 'Pg is down!')


@dp.message_handler(commands=['start_game'])
async def start_game_cmd(message: types.Message):
    if message.chat.id == MAIN_ADMIN:
        global IS_STARTED
        IS_STARTED = True
        await bot.send_message(message.chat.id, '*GAME IS STARTED!!!*', parse_mode='Markdown')
        async with db_engine.acquire() as conn:
            tg_ids = await get_all_tg_ids(conn)
            from game import send_to
            msg = start_game_msg()
            await send_to(tg_ids, msg, conn, bot)

            teams = await get_team_with_members(conn)
            for c_team in teams:
                team_name = c_team[0]
                teammates = c_team[1]
                msg = your_teammates(team_name, teammates)
                for teammate in teammates:
                    await bot.send_message(teammate[2], msg['body']['text'])
        from game import start_game
        await start_game(db_engine, bot)


@dp.message_handler(commands=['delete_game'])
async def delete_game_cmd(message: types.Message):
    if message.chat.id == MAIN_ADMIN:
        global IS_STARTED
        IS_STARTED = False
        await bot.send_message(message.chat.id, '*Game deleted!*', parse_mode='Markdown')
        async with db_engine.acquire() as conn:
            await db_delete_game(conn)


@dp.message_handler(commands=['freeze_game'])
async def freeze_game_cmd(message: types.Message):
    if message.chat.id == MAIN_ADMIN:
        global IS_STARTED
        IS_STARTED = False
        await bot.send_message(message.chat.id, '*Game frozen*', parse_mode='Markdown')
        async with db_engine.acquire() as conn:
            await freeze_game(conn)


@dp.message_handler(commands=['submit'])
async def submit_answer_cmd(message: types.Message):
    if not IS_STARTED:
        await bot.send_message(message.chat.id, 'На все свій час володарю…')
        return
    async with db_engine.acquire() as conn:
        if not await check_user_exist(conn, message.from_user.id):
            return
        answer = message.get_args()
        is_correct = await check_and_submit(conn, message.from_user.id, answer)
        if not is_correct:
            await bot.send_message(message.chat.id, 'На жаль, відповідь неправильна ((')
            return
        await team_next_task(conn, message.from_user.id)
        await bot.send_message(message.chat.id, 'Йоу, це правильна відповідь!')
        tg_ids = await get_all_teammates_tgs(conn, message.from_user.id)
        msg = correct_answer_template(message.from_user.username, message.from_user.full_name)
        for tg_id in tg_ids:
            await bot.send_message(tg_id, msg['body']['text'])
        await send_next_tesk(message.from_user.id, conn)


async def send_next_tesk(tg_id, conn):
    from game import send_to
    tg_ids = await get_all_teammates_tgs(conn, tg_id)
    if not await check_if_not_finished_by_user(conn, tg_id):
        task = await get_team_current(conn, tg_id)
        msg = msg_template(task, 600, None, 1200, None)
        msg = {
            'type': 'text',
            'body': {
                'text': msg,
                'parse_mode': 'Markdown'
            }
        }
    else:
        db_row = await get_team_time_and_name(conn, tg_id)
        team_name = db_row[0]
        team_time = int(db_row[1].total_seconds())
        teammates = await get_teammates_by_team_id(conn, db_row[2])
        msg = grats_msg_template(team_name, team_time, teammates)
        await send_to(tg_ids, msg, conn, bot)
        msg = final_msg_template()

    await send_to(tg_ids, msg, conn, bot)


@dp.message_handler(commands=['send_to_all'])
async def send_to_all(message: types.Message):
    if message.chat.id == MAIN_ADMIN:
        text = message.get_args().replace('$', '*').replace('^', '_')
        async with db_engine.acquire() as conn:
            tg_ids = await get_all_tg_ids(conn)
            for tg_id in tg_ids:
                await bot.send_message(tg_id, text, parse_mode='Markdown')


@dp.message_handler(commands=['my_id'])
async def get_my_tg_id(message: types.Message):
    await bot.send_message(message.chat.id, f'Id: {message.from_user.id}')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_filter(message: types.Message):
    await bot.forward_message(MAIN_ADMIN, message.chat.id, message.message_id, True)


# @dp.message_handler(commands=['will_be_edited'])
# async def test_cmd(message: types.Message):
#     msg = await bot.send_message(message.from_user.id, 'Hello')
#     await asyncio.sleep(2)
#     await bot.edit_message_text('Xyu', message.from_user.id, msg.message_id)

if __name__ == '__main__':
    load_env()

    set_up_logging(os.getenv('LOG_FILE'), os.getenv('VERBOSE') == 'True')

    if os.getenv('INIT_DB') == 'True':
        from db.init_db import init_db

        logging.warning('Forced to reinitialize db...')
        init_db()

    db_engine = loop.run_until_complete(init_pg())

    try:
        executor.start_polling(dp, skip_updates=False, loop=loop)
    finally:
        loop.run_until_complete(close_pg(db_engine))
