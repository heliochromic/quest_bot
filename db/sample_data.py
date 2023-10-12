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
        'task_num': 1,
        'name': "Чому дорівнює фреш?",
        'description': '_... курсу приготуватись!_',
        'last_msg': '_Першому_ курсу приготуватись!',
        'answer': '001',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 2,
        'name': "Афон чи *Самсон*?",
        'description': 'Знайдіть Самсона з 🦁',
        'last_msg': 'Прямуйте до фонтану Самсон і Ротонда',
        'answer': '648',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 3,
        'name': "На реконструкції довше за Староакадемічний. [дата побудови] - [дата початку реконструкції] = *ОК*.",
        'description': 'Точно *гостинніший* третього корпуса',
        'last_msg': 'Success status code',
        'answer': '200',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 4,
        'name': "Провести всю неділю на *КМЦ* звучить *_спокусливо_*, але за вами слідкують.",
        'description': 'У стін є вуха, а у дерев – (https://www.youtube.com/shorts/AW5kwx9Bsdc)',
        'last_msg': 'Порахуйте очі намальовані на деревах на кмц',
        'answer': '011',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 5,
        'name': "[Це що?](https://t.me/buddynaukma/463), а [це що?](https://i.imgur.com/dJcQea5.jpg)",
        'description': 'салат? шифр? хто ти?',
        'last_msg': 'любите хокку? Велике дерево, зручна лавка, сад, сам, колишній портер',
        'answer': '315',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 6,
        'name': "“Non-geographic numbers charged at standard geographic area code rates (introduced in 2007) – x qhhg wr jr wr vsdvnd wkluwhhq",
        'description': 'Григорій Савич Єяаіараґц. До речі, а ви читали зранку цмгяґае?',
        'last_msg': 'Вася дуже любить мєми, а який твій улюблений? Покажи.',
        'answer': '195',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 7,
        'name': "А куди б сходити *цього місяця*?",
        'description': 'який твій улюблений попкорн?',
        'last_msg': 'Біля кінотеатра "Жовтень" на вас чекають',
        'answer': '901',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 8,
        'name': "Що _посієш_ – те й пожнеш.",
        'description': 'Де б купити свіжих овочів?',
        'last_msg': 'Вам потрібно до житнього ринку.',
        'answer': '777',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 9,
        'name': "імпорт Ноти;\n   функ отримати_слово():\n  	      стрічка фі = “фі”;\n         ретюрн фі + Ноти[0];",
        'description': 'Знайдіть найбільш айтішну студ організацію',
        'last_msg': 'Знайдіть FIdo',
        'answer': '129',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 10,
        'name': "Їх у родині багато: Сарна, Аксис, Гемал. Але на Подолі він лише один.",
        'description': 'Знайдеш на стіні',
        'last_msg': 'Ідіть до проїжджої частини навпроти мурала з оленем на вулиці Волоської',
        'answer': '264',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 11,
        'name': "Pour manger? - Allons au _Блукач_",
        'description': 'Заблукав на вулиці іншого блукача',
        'last_msg': 'Бариста у Вагабонді не такий простий як здається на перший погляд',
        'answer': '583',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 12,
        'name': "[завдання](https://i.imgur.com/QkDReY2.jpg)",
        'description': 'Як добре, що прапор _Каннади_ тут ні до чого. Пошукайте, як справжні каннадійці пишуть цифри.',
        'last_msg': 'Зашифровані древньою мовою каннада координати привели вас до кафе 119, подивіться на неї ближче до дороги',
        'answer': '119',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 13,
        'name': "Архангел тіней забутих родичів назавжди закарбувався у гербі. Прямуйте в кав'ярню за вулицею [третього засновника], 25.",
        'description': 'Згадай засновників Києва',
        'last_msg': 'Залежність страшна річ, особливо, коли вона від еспресо, а як кличуть залежних від еспресо?',
        'answer': '438',
        'need_to_approved': False,
        'is_final': False
    },
    {
        'task_num': 14,
        'name': "На Подолі їх два: один зверху, другий знизу, паралельні один одному і перетинаються двічі. "
                "Вам потрібна точка ближче до Дніпра. Там і зустрінемось на фінальне завдання.",
        'description': 'Перетин вулиць Нижній та Верхній вал.',
        'last_msg': 'Перетин вулиць Нижній та Верхній вал',
        'answer': '947',
        'need_to_approved': False,
        'is_final': True
    }
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
