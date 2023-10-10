import json


def get_tasks():
    return [
        {
            'task_num': 0,
            'name': "Entrypoint, the answer is *123*  [google](https://google.com)",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 32.1234
                }
            }),
            'description': 'Desc',
            'answer': '123',
            'need_to_approved': False,
            'last_msg': 'Last msg of the task',
            'is_final': False
        },
        {
            'task_num': 1,
            'name': 'Not an Entrypoint: 1233',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 31.1234
                }
            }),
            'description': 'Desc one',
            'answer': '1233',
            'need_to_approved': True,
            'last_msg': 'Last msg of the task',
            'is_final': False
        },
        {
            'task_num': 2,
            'name': 'Ne Entrypoint: 1234',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 34.1234
                }
            }),
            'description': 'desc Desc',
            'answer': '1234',
            'last_msg': 'Last msg of the task',
            'need_to_approved': False,
            'is_final': False
        },
        {
            'task_num': 3,
            'name': 'Finish point: 12345',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '12345',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': False
        },
        {
            'task_num': 4,
            'name': 'NE  inish point: 123456',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '123456',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': False
        },
        {
            'task_num': 5,
            'name': 'nish point: 1234567',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '1234567',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': False
        },
        {
            'task_num': 6,
            'name': 'inish point: 12345',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '12345',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': False
        },
        {
            'task_num': 7,
            'name': 'point: 2345',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '2345',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': False
        },
        {
            'task_num': 8,
            'name': 'Finish point: 12345',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.1234,
                    "longitude": 33.1234
                }
            }),
            'description': 'Desc of finish task',
            'answer': '12345',
            'last_msg': 'Last msg of the task',
            'need_to_approved': True,
            'is_final': True
        },
    ]

def get_prod_tasks():
    return [
        {
            'task_num': 0,
            'name': "Чому дорівнює фреш?",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4667,
                    "longitude": 30.52286
                }
            }),
            'description': '_... курсу приготуватись!_',
            'answer': '001',
            'need_to_approved': False,
            'last_msg': '_Першому_ курсу приготуватись!',
            'is_final': False
        },
        {
            'task_num': 1,
            'name': "Їх було *багато*, були єдині, були _розколоті_. Де їх *зараз* можна знайти?",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.467362,
                    "longitude": 30.520042
                }
            }),
            'description': 'Хто ж вони? Один був покровителем Київської братської школи, інший - сонцем. Двох можна зараз знайти у вас в кишенях. А відповідь шукайте навпроти.',
            'answer': '648',
            'need_to_approved': False,
            'last_msg': 'Навпроти музея Гетьманства через дорогу намальовано код',
            'is_final': False
        },
        {
            'task_num': 2,
            'name': "На реконструкції довше за Староакадемічний. Дата побудови - дата початку реконструкції = *ОК* Вітаю!",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46409,
                    "longitude": 30.51862
                }
            }),
            'description': 'Ви успішно підписали *контракт на покупку* вищої освіти!',
            'answer': '200',
            'need_to_approved': False,
            'last_msg': 'Success status code',
            'is_final': False
        },
        {
            'task_num': 3,
            'name': "Провести всю неділю на *КМЦ* звучить *_спокусливо_*, але вам [звісточка](https://youtu.be/0KuyYPl2mFk)",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4651,
                    "longitude": 30.5216
                }
            }),
            'description': 'tentator = спокусник',
            'answer': '017',
            'need_to_approved': False,
            'last_msg': 'Порахуйте вікна на фронтовій частині Сербського посольства',
            'is_final': False
        },
        {
            'task_num': 4,
            'name': "[Це що?](https://t.me/buddynaukma/463), а [це що?](https://i.imgur.com/dJcQea5.jpg)",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4677,
                    "longitude": 30.52408
                }
            }),
            'description': 'Куди б написати заяву про відрахування?',
            'answer': '315',
            'need_to_approved': False,
            'last_msg': 'Твоя довідка про навчання в кабінеті деканату факультету інформатики. Гугл в помощ',
            'is_final': False
        },
        {
            'task_num': 5,
            'name': """Иеа ґвщцп тра мцвяв, еас їфуюез шш, ц иеа шш їфуюез, еас мляаїю мг тгргєецп іжюеюєн, иажц хаімл ілм л хґціцієн угхґлнїзмющ. 

Еаул таерлума мц їаяцолф: Тгера Єцдцсґцжмюс

Тобі потрібно на локацію - Еаул таерлума мц їаяцолф""",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46315,
                    "longitude": 30.51852
                }
            }),
            'description': 'Григорій Савич Єяаіараґц. До речі, а ви читали зранку цмгяґае?',
            'answer': '195',
            'need_to_approved': False,
            'last_msg': 'Вася дуже любить мєми, а який твій улюблений? Покажи.',
            'is_final': False
        },
        {
            'task_num': 6,
            'name': 'А після карантину запросиш мене в кіно?',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46841,
                    "longitude": 30.51018
                }
            }),
            'description': '24.*10*.21',
            'answer': '901',
            'need_to_approved': False,
            'last_msg': 'Біля кінотеатра "Жовтень" на вас чекають',
            'is_final': False
        },
        {
            'task_num': 7,
            'name': 'Що _посієш_.. де б купити свіжих овочів?',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4643,
                    "longitude": 30.51139
                }
            }),
            'description': 'Вам потрібен ринок.',
            'answer': '777',
            'need_to_approved': False,
            'last_msg': 'Біля житнього ринку намальований код 777',
            'is_final': False
        },
        {
            'task_num': 8,
            'name': 'Під час ремонту за книжковими шафами знайшли раритетний револьвер. Про це повідомив радник '
                    'міністра МВС Михайло Апостол.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46497,
                    "longitude": 30.51893
                }
            }),
            'description': 'Ти не читаєш *новини*?(',
            'answer': '129',
            'need_to_approved': False,
            'last_msg': 'На вас чекають біля Староакадемічного корпусу на вулиці Сковороди',
            'is_final': False
        },
        {
            'task_num': 9,
            'name': 'Їх у родині багато: Сарна, Аксис, Гемал. Але на Подолі він лише один.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46781,
                    "longitude": 30.51813
                }
            }),
            'description': 'Знайдеш на стіні',
            'answer': '264',
            'need_to_approved': False,
            'last_msg': 'Код намальовано біля проїжджої частини навпроти мурала з оленем на вулиці Волоської',
            'is_final': False
        },
        {
            'task_num': 10,
            'name': 'Pour manger? - Allons au _Блукач_',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46625,
                    "longitude": 30.52066
                }
            }),
            'description': 'Заблукав на вулиці іншого блукача',
            'answer': '583',
            'need_to_approved': False,
            'last_msg': 'Бариста у Вагабонді не такий простий як здається на перший погляд',
            'is_final': False
        },
        {
            'task_num': 11,
            'name': '[завдання](https://i.imgur.com/QkDReY2.jpg)',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46477,
                    "longitude": 30.5221
                }
            }),
            'description': 'Як добре, що прапор _Каннади_ тут ні до чого.',
            'answer': '119',
            'need_to_approved': False,
            'last_msg': 'Зашифровані древньою мовою каннада координати привели вас до кафе 119, подивіться на неї '
                        'ближче до дороги',
            'is_final': False
        },
        {
            'task_num': 12,
            'name': 'Архангел тіней забутих родичів назавжди закарбувався у гербі. Прямуйте в кав\'ярню за вулицею '
                    'третього засновника, 25. [фото](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8'
                    '/Coat_of_arms_of_Kiev.svg/180px-Coat_of_arms_of_Kiev.svg.png)',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46679,
                    "longitude": 30.51593
                }
            }),
            'description': 'Згадай засновників Києва',
            'answer': '438',
            'need_to_approved': False,
            'last_msg': 'Залежність страшна річ, особливо, коли вона від еспресо, а як кличуть залежних від еспресо?',
            'is_final': False
        },
        {
            'task_num': 13,
            'name': 'На Подолі їх два: один зверху, другий знизу, паралельні один одному і перетинаються двічі. Вам потрібна точка ближче до Дніпра. Там і зустрінемось на фінальне завдання.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.47115,
                    "longitude": 30.51983
                }
            }),
            'description': 'Перетин вулиць Нижній та Верхній вал.',
            'answer': '947',
            'need_to_approved': False,
            'last_msg': 'Перетин вулиць Нижній та Верхній вал.',
            'is_final': True
        },
    ]


def get_test_tasks():
    return [
        {
            'task_num': 0,
            'name': "Що не так з _назвою_?",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4667,
                    "longitude": 30.52286
                }
            }),
            'description': '_Кіберпанк …_',
            'answer': '2077',
            'need_to_approved': False,
            'last_msg': '_Кіберпанк 2077_ *C2077*',
            'is_final': False
        },
        {
            'task_num': 1,
            'name': "_КМЦ_: ліхтарі + лавки = ?",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4667,
                    "longitude": 30.52286
                }
            }),
            'description': '_КМЦ_: сходи + памятник = 11',
            'answer': '46',
            'need_to_approved': False,
            'last_msg': 'Це математична загадка xD *C46*',
            'is_final': False
        },
        {
            'task_num': 2,
            'name': "Стою під сонцем, дивлюсь котра година, а позаду?",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46531,
                    "longitude": 30.52098
                }
            }),
            'description': 'Який годинник _не має_ стрілок?\n\n_(Код - це відповідь на це завдання, тому йти на саму '
                           'локацію необов\'язково, якщо ви її добре пам\'ятаєте :))_',
            'answer': '010',
            'need_to_approved': False,
            'last_msg': 'Позаду однієї зі сторін сонячного годинника НаУКМА знаходиться .. корпус *C10*',
            'is_final': False
        },
        {
            'task_num': 3,
            'name': "Вам [звісточка](https://youtu.be/e9y21Mnmpfw)",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4664,
                    "longitude": 30.52243
                }
            }),
            'description': 'Вулиця: Г. Сковороди',
            'answer': '725',
            'need_to_approved': False,
            'last_msg': 'Звісточка привела вас до FIdo (колишня назва usic), один з олдів на вас там чекає *C725*',
            'is_final': False
        },
        {
            'task_num': 4,
            'name': "[Це що?](https://t.me/buddynaukma/463), а [це що?](https://i.imgur.com/dJcQea5.jpg)",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4677,
                    "longitude": 30.52408
                }
            }),
            'description': 'Напис на щось натякає, у *кого б* спитати?',
            'answer': '321',
            'need_to_approved': False,
            'last_msg': 'Сьогодні вже багато разів /start\'ували? *C321*',
            'is_final': False
        },
        {
            'task_num': 5,
            'name': """Иеа ґвщцп тра мцвяв, еас їфуюез шш, ц иеа шш їфуюез, еас мляаїю мг тгргєецп іжюеюєн, иажц хаімл ілм л хґціцієн угхґлнїзмющ. 

Еаул таерлума мц їаяцолф: Тгера Єцдцсґцжмюс

Тобі потрібно на локацію - Еаул таерлума мц їаяцолф""",
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46315,
                    "longitude": 30.51852
                }
            }),
            'description': 'Григорій Савич Єяаіараґц. До речі, а ви читали зранку цмгяґае?',
            'answer': '195',
            'need_to_approved': False,
            'last_msg': 'Розкажіть анекдот Дєду біля памятника Сагайдачного *C195*',
            'is_final': False
        },
        {
            'task_num': 6,
            'name': 'За 2 місяці сходимо в кіно?',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46841,
                    "longitude": 30.51018
                }
            }),
            'description': 'Зараз _серпень_',
            'answer': '901',
            'need_to_approved': False,
            'last_msg': 'Біля кіноеатра "Жовтень" на вас чекають *C901*',
            'is_final': False
        },
        {
            'task_num': 7,
            'name': 'Що посієш.. де б купити свіжих овочів?',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4643,
                    "longitude": 30.51139
                }
            }),
            'description': 'Вам потрібен ринок.',
            'answer': '777',
            'need_to_approved': False,
            'last_msg': 'Біля житнього ринку намальований код С777',
            'is_final': False
        },
        {
            'task_num': 8,
            'name': 'Під час ремонту за книжковими шафами знайшли раритетний револьвер. Про це повідомив радник '
                    'міністра МВС Михайло Апостол.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46497,
                    "longitude": 30.51893
                }
            }),
            'description': 'Ти не любиш новини?(',
            'answer': '129',
            'need_to_approved': False,
            'last_msg': 'На вас чекають біля староакадемічного корпусу на вулиці Сковороди *C129*',
            'is_final': False
        },
        {
            'task_num': 9,
            'name': 'Їх у родині багато: Сарна, Аксис, Гемал. Але на подолі він лише один.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46781,
                    "longitude": 30.51813
                }
            }),
            'description': 'Знайдеш на стіні',
            'answer': '264',
            'need_to_approved': False,
            'last_msg': 'Код намальовано біля проїжджої частини навпроти мурала з оленем на вулиці Волоської *C264*',
            'is_final': False
        },
        {
            'task_num': 10,
            'name': 'Pour manger? - Блукач',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46625,
                    "longitude": 30.52066
                }
            }),
            'description': 'Заблукав на вулиці іншого блукача',
            'answer': '583',
            'need_to_approved': False,
            'last_msg': 'Бариста у Вагабонді не такий простий як здається на перший погляд *C583*',
            'is_final': False
        },
        {
            'task_num': 11,
            'name': '[завдання](https://i.imgur.com/QkDReY2.jpg)',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46477,
                    "longitude": 30.5221
                }
            }),
            'description': 'Як добре, що прапор _Каннади_ тут ні до чого.',
            'answer': '119',
            'need_to_approved': False,
            'last_msg': 'Зашифровані древньою мовою координати привели вас до кафе 119, подивіться на неї ближче до '
                        'дороги *C119*',
            'is_final': False
        },
        {
            'task_num': 12,
            'name': 'Архангел тіней забутих родичів назавжди закарбувався у гербі. Прямуйте в кав\'ярню за вулицею '
                    'третього засновника 25. [фото](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8'
                    '/Coat_of_arms_of_Kiev.svg/180px-Coat_of_arms_of_Kiev.svg.png)',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.46679,
                    "longitude": 30.51593
                }
            }),
            'description': 'Згадай засновників Києва',
            'answer': '438',
            'need_to_approved': False,
            'last_msg': 'Залежність страшна річ, особливо, коли вона від еспресо, а як кличуть залежних від еспресо? '
                        '*C438*',
            'is_final': False
        },
        {
            'task_num': 13,
            'name': 'Цифровий завідувач розкладом могилянки відгукується ще й на імена /черепах.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.4667,
                    "longitude": 30.52286
                }
            }),
            'description': 'Ти що не знаєш цього [завідувача](https://www.youtube.com/watch?v=fVHz26C7qH0) чи /alma\'у',
            'answer': '171',
            'need_to_approved': False,
            'last_msg': '@KmaSchedulerBot /alma *C171*',
            'is_final': False
        },
        {
            'task_num': 14,
            'name': 'Є на контрактовій дві протилежності. І перетинаються вони теж у двох місцях - вам потрібна точка '
                    'ближче до Дніпра. Там і зустрінемось на фінальне завдання.',
            'location': json.dumps({
                "type": "location",
                "body": {
                    "latitude": 50.47115,
                    "longitude": 30.51983
                }
            }),
            'description': 'Перетин вулиць Нижній та Верхній вал.',
            'answer': '947',
            'need_to_approved': False,
            'last_msg': 'Перетин вулиць Нижній та Верхній вал.',
            'is_final': True
        },
    ]
