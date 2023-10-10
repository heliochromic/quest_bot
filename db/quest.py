import json


def get_prod_tasks():
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
            'last_msg': '_Кіберпанк 2077_',
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
            'description': 'Хто ж вони? Один був покровителем Київської братської школи, інший - [сонцем]('
                           'https://lmgtfy.com/?q=%D1%81%D0%BE%D0%BD%D1%86%D0%B5+%D0%B2+%D1%96%D1%81%D1%82%D0%BE%D1'
                           '%80%D1%96%D1%97+%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8&iie=1). Двох можна '
                           'зараз знайти у вас в кишенях.',
            'answer': '648',
            'need_to_approved': False,
            'last_msg': 'Біля музея Гетьманства намальовано код',
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
            'description': 'Який годинник _не має_ стрілок?',
            'answer': '010',
            'need_to_approved': False,
            'last_msg': 'Позаду однієї зі сторін сонячного годинника НаУКМА знаходиться .. корпус',
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
            'last_msg': 'Звісточка привела вас до FIdo (колишня назва usic), один з олдів на вас там чекає',
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
            'last_msg': 'Сьогодні вже багато разів /start\'ували?',
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
            'last_msg': 'Розкажіть анекдот Дєду біля памятника Сагайдачного',
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
            'last_msg': 'Біля кіноеатра "Жовтень" на вас чекають',
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
            'last_msg': 'На вас чекають біля староакадемічного корпусу на вулиці Сковороди',
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
            'last_msg': 'Код намальовано біля проїжджої частини навпроти мурала з оленем на вулиці Волоської',
            'is_final': False
        },
        {
            'task_num': 10,
            'name': 'Pour manger? - _Блукач_',
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
            'last_msg': 'Зашифровані древньою мовою Каннада координати привели вас до кафе 119, подивіться на неї '
                        'ближче до дороги',
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
            'last_msg': 'Залежність страшна річ, особливо, коли вона від еспресо, а як кличуть залежних від еспресо?',
            'is_final': False
        },
        {
            'task_num': 13,
            'name': 'Є на Подолі дві протилежності. І перетинаються вони теж у двох місцях - вам потрібна точка '
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