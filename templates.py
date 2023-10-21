from time import gmtime, strftime


def start_msg():
    msg = {
        'type': 'text',
        'body': {
            'text': '*ЦИФРОВА* гра скоро почнеться!, назва квесту: '
                    '*гра в Фреша*\n\nЩоб зареєструватися в команді, введи /connect <код команди> ('
                    'без кутових лапок). Пліч-о-пліч з цими людьми тобі доведеться пройти багато кроків і відповісти '
                    'на багато запитань. Тож не будь як 067 та довірся своїм Бадді та команді. '
                    '\n\nЩоб відповісти на поставлене питання, використай команду /submit <відповідь> (без кутових '
                    'лапок). Будь-хто з членів команди може відповісти на питання. Кількість спроб необмежена. Щойно '
                    'Бот отримає правильну відповідь, ти дізнаєшся про це і отримаєш наступне завдання. Через '
                    'деякий час після отримання тобою завдання, Бот дасть підказку. Якщо це не допоможе — ще за '
                    'деякий час місце, де шукати відповіді. Ще згодом — наступне питання. Довіряй своїй чуйці та '
                    'співкомандникам; кооперуйся для швидшого досягання мети.',
            'parse_mode': 'Markdown'
        }
    }
    return msg


def start_game_msg():
    return {
        'type': 'text',
        'body': {
            'text': f'*ГРА ПОЧИНАЄТЬСЯ*!!!'
                    f'\nНезабаром ти отримаєш перше завдання (підказка: воно на розминочку), ти вже *готовий*?',
            'parse_mode': 'Markdown'
        }
    }


def your_teammates(team_name, teammates):
    res = []
    for teammate in teammates:
        username = teammate[0]
        full_name = teammate[1]
        res.append(f'{full_name} {("(@" + username + ")") if username is not None else ""}')

    return {
        'type': 'text',
        'body': {
            'text': f'Команда: {team_name}, а в ній славні молодці: {", ".join(res)}',
            'parse_mode': None
        }
    }


def correct_answer_template(tg_user, tg_name):
    return {
        'type': 'text',
        'body': {
            'text': f'Правильна відповідь прилетіла від '
                    f'{tg_name} {("(@" + tg_user + ")") if tg_user is not None else ""}',
            'parse_mode': None
        }
    }


def msg_template(text, time_first, first_p, time_second, second_p):
    return f"""*ЗАВДАННЯ!*

{text}

*{strftime("%M:%S", gmtime(time_first))}*: {'_Ще недоступне_' if first_p is None else first_p}
*{strftime("%M:%S", gmtime(time_second))}*: {'_Ще недоступне_' if second_p is None else second_p}
    """


def grats_msg_template(team_name, team_time, teammates):
    res = []
    for teammate in teammates:
        username = teammate[0]
        full_name = teammate[1]
        res.append(f'{full_name} {("(@" + username + ")") if username is not None else ""}')

    msg = {
        'type': 'text',
        'body': {
            'text': f"""ВІТАЄМО!

Твоя команда {team_name} фінішувала з часом: {strftime("%H:%M:%S", gmtime(team_time))}!!!
Неперевершений склад команди: {", ".join(res)}
""",
            'parse_mode': None
        }
    }
    return msg


def final_msg_template():
    msg = {
        'type': 'text',
        'body': {
            'text': f"""Сподіваємось, що тобі все сподобалося. Фідбек щодо самого квесту ти можеш (а ще краще _повинен_) залишити своїм Бадді, якщо хочеш, щоб ми проводили таке в подальшому і ще й краще. 

Не забудь подякувати своїм *Бадді*!

Спосібо за бота: @kirillkundik

Окреме пасіба поважним товаріщам @heliochromatic та @itsgreedyjew (можна в інсті підписаться якщо що)

""",
            'parse_mode': 'Markdown'
        }
    }
    return msg
