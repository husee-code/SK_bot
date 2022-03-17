from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# 37
func_txt = "——————Выбор функций——————"
greet_text = """Добро пожаловать в наш сервис! 
Здесь вы можете отправить заявку на внесение изменений в готовые полисы Осаго. 

Далее вы увидите список страховых компаний и доступных на сегодняшний день изменений. Наши возможности постоянно расширяются.
Если вы не нашли свой вариант - отправьте "уникальную заявку" и с вами свяжутся.

Среднее время обработки заказа: 1-2 дня. 
Сервис работает по предоплате. Если нужно внести изменение - оплачиваем, и делаем. За нас говорит наша репутация в мире Страхования. Мы ни от кого не прячемся - наши контакты в разделе "Связь с нами". Мы здесь собрались для плодотворного сотрудничества. 

Также, в разделе "Связь с нами" - вы всегда можете связаться с создателями данного сервиса, для решения не стандартных вопросов, обсуждения скидок при наличии объёмов, либо предложений по сотрудничеству. 

С ув. Аллигатор team."""

prices_dict = \
    {
        'Росгосстрах':
            {
                "Продление периода": 3000,
                "Внесение ВУ": 3000,
                'Внести/поменять гос. номер': 3000,
                'Смена собственника': 3000,
                'Исправление ошибки': 3000,
                'Рассторжение полиса': 3000,
                'Смена цели использования': 3000
            },
        'Ингосстрах':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Смена собственника': 1500,
                'Исправление ошибки': 1500
            },
        'ВСК':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Смена собственника': 1500,
                'Исправление ошибки': 1500,
                'Рассторжение полиса': 1500,
                'Смена цели использования': 2000
            },
        'РЕСО':
            {
                'Продление периода': 3000,
                'Внесение ВУ': 3000,
                'Внести/поменять гос. номер': 3000,
                'Смена собственника': 5000,
                'Смена цели использования': 5500,
                'Исправление ошибки': 3000
            },
        'Согаз':
            {
                "Продление периода": 3000,
                "Внесение ВУ": 3000,
                "Внести/поменять гос. номер": 3000,
                "Смена собственника": 3000,
                "Исправление ошибки": 3000
            },
        'Сбер Страхование': {
            'Продление периода': 1500,
            'Внесение ВУ': 1500,
            'Внести/поменять гос. номер': 1500,
            'Исправление ошибки': 1500
            },
        'Альфа Страхование':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Исправление ошибки': 1500
            },
        'МАКС':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Исправление ошибки': 1500
            },
        'Зетта Страхование':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Исправление ошибки': 1500
            },
        'Тинькофф Страхование':
            {
                'Продление периода': 1500,
                'Внесение ВУ': 1500,
                'Внести/поменять гос. номер': 1500,
                'Смена собственника': 1500,
                'Исправление ошибки': 1500
            }
    }


def getAmount(sk, option):
    return f'| {prices_dict[sk][option]}'


sk_list = [
    InlineKeyboardButton(text='Росгосстрах', callback_data='Росгосстрах'),
    InlineKeyboardButton(text='Ингосстрах', callback_data='Ингосстрах'),
    InlineKeyboardButton(text='ВСК', callback_data='ВСК'),
    InlineKeyboardButton(text='РЕСО', callback_data='РЕСО'),
    InlineKeyboardButton(text='Согаз', callback_data='Согаз'),
    InlineKeyboardButton(text='Сбер Страхование', callback_data='Сбер Страхование'),
    InlineKeyboardButton(text='Альфа Страхование', callback_data='Альфа Страхование'),
    InlineKeyboardButton(text='Зетта Страхование', callback_data='Зетта Страхование'),
    InlineKeyboardButton(text='МАКС', callback_data='МАКС'),
    InlineKeyboardButton(text='Тинькофф Страхование', callback_data='Тинькофф Страхование')]

keyboards_dict = \
    {'Росгосстрах':
         {"alert": "Можно внести изменения в любой полис(БСО, еБСО, эл.полис)",
          "buttons":
              {'Продление периода': InlineKeyboardButton(
                  text=f'Продление периода {getAmount("Росгосстрах", "Продление периода")}',
                  callback_data='Продление периода'),
                  'Внесение ВУ': InlineKeyboardButton(
                      text=f'Внесение ВУ {getAmount("Росгосстрах", "Внесение ВУ")}',
                      callback_data='Внесение ВУ'),
                  'Внести/поменять гос. номер': InlineKeyboardButton(
                      text=f'Внести/поменять гос. номер {getAmount("Росгосстрах", "Внести/поменять гос. номер")}',
                      callback_data='Внести/поменять гос. номер'),
                  'Смена собственника': InlineKeyboardButton(
                      text=f'Смена собственника {getAmount("Росгосстрах", "Смена собственника")}',
                      callback_data='Смена собственника'),
                  'Исправление ошибки': InlineKeyboardButton(
                      text=f'Исправление ошибки {getAmount("Росгосстрах", "Исправление ошибки")}',
                      callback_data='Исправление ошибки'),
                  'Рассторжение полиса': InlineKeyboardButton(
                      text=f'Рассторжение полиса {getAmount("Росгосстрах", "Рассторжение полиса")}',
                      callback_data='Рассторжение полиса'),
                  'Смена цели использования': InlineKeyboardButton(
                      text=f'Смена цели использования {getAmount("Росгосстрах", "Смена цели использования")}',
                      callback_data='Смена цели использования')}},
     'Ингосстрах':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("Ингосстрах", "Продление периода")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(
                  text=f'Внесение ВУ {getAmount("Ингосстрах", "Внесение ВУ")}',
                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(
                  text=f'Внести/поменять гос. номер {getAmount("Ингосстрах", "Внести/поменять гос. номер")}',
                  callback_data='Внести/поменять гос. номер'),
              'Смена собственника': InlineKeyboardButton(
                  text=f'Смена собственника {getAmount("Ингосстрах", "Смена собственника")}',
                  callback_data='Смена собственника'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("Ингосстрах", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},
     'ВСК':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("ВСК", "Продление периода")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(text=f'Внесение ВУ {getAmount("ВСК", "Внесение ВУ")}',
                                                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(
                  text=f'Внести/поменять гос. номер {getAmount("ВСК", "Внести/поменять гос. номер")}',
                  callback_data='Внести/поменять гос. номер'),
              'Смена собственника': InlineKeyboardButton(
                  text=f'Смена собственника {getAmount("ВСК", "Смена собственника")}',
                  callback_data='Смена собственника'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("ВСК", "Исправление ошибки")}',
                  callback_data='Исправление ошибки'),
              'Рассторжение полиса': InlineKeyboardButton(
                  text=f'Рассторжение полиса {getAmount("ВСК", "Рассторжение полиса")}',
                  callback_data='Рассторжение полиса'),
              'Смена цели использования': InlineKeyboardButton(
                  text=f'Смена цели использования {getAmount("ВСК", "Смена цели использования")}',
                  callback_data='Смена цели использования')}},
     'РЕСО':
         {"alert": "Можно внести изменения в любой полис(БСО, еБСО, эл.полис)",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("РЕСО", "Продление периода")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(text=f'Внесение ВУ {getAmount("РЕСО", "Внесение ВУ")}',
                                                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(
                  text=f'Внести/поменять гос. номер {getAmount("РЕСО", "Внести/поменять гос. номер")}',
                  callback_data='Внести/поменять гос. номер'),
              'Смена собственника': InlineKeyboardButton(
                  text=f'Смена собственника {getAmount("РЕСО", "Смена собственника")}',
                  callback_data='Смена собственника'),
              'Смена цели использования': InlineKeyboardButton(
                  text=f'Смена цели использования {getAmount("РЕСО", "Смена цели использования")}',
                  callback_data='Смена цели использования'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("РЕСО", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},

     'Согаз':
         {"alert": "Изменения вносят на бланки БСО, возможна доставка полисов на любой регион",
          "buttons": {"Продление периода": InlineKeyboardButton(
              text=f"Продление периода {getAmount('Согаз', 'Продление периода')}",
              callback_data="Продление периода"),
              "Внесение ВУ": InlineKeyboardButton(text=f"Внесение ВУ {getAmount('Согаз', 'Продление периода')}",
                                                  callback_data="Внесение ВУ"),
              "Внести/поменять гос. номер": InlineKeyboardButton(
                  text=f"Внести/поменять гос. номер {getAmount('Согаз', 'Внести/поменять гос. номер')}",
                  callback_data="Внести/поменять гос. номер"),
              "Смена собственника": InlineKeyboardButton(
                  text=f"Смена собственника {getAmount('Согаз', 'Смена собственника')}",
                  callback_data="Смена собственника"),
              "Исправление ошибки": InlineKeyboardButton(
                  text=f"Исправление ошибки {getAmount('Согаз', 'Исправление ошибки')}",
                  callback_data="Исправление ошибки")}},
     'Сбер Страхование':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("Сбер Страхование", "Продление периода")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(
                  text=f'Внесение ВУ {getAmount("Сбер Страхование", "Внесение ВУ")}',
                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                                                      f' {getAmount("Сбер Страхование", "Внести/поменять гос. номер")}',
                                                                 callback_data='Внести/поменять гос. номер'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("Сбер Страхование", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},
     'Альфа Страхование':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("Альфа Страхование", "Продление периода")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(
                  text=f'Внесение ВУ {getAmount("Альфа Страхование", "Внесение ВУ")}',
                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(text=f'Внести/поменять гос. номер '
                                                                      f'{getAmount("Альфа Страхование", "Внести/поменять гос. номер")}',
                                                                 callback_data='Внести/поменять гос. номер'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("Альфа Страхование", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},
     'МАКС':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {'Продление периода': InlineKeyboardButton(
              text=f'Продление периода {getAmount("МАКС", "Исправление ошибки")}',
              callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(
                  text=f'Внесение ВУ {getAmount("МАКС", "Внесение ВУ")}', callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(
                  text=f'Внести/поменять гос. номер {getAmount("МАКС", "Внести/поменять гос. номер")}',
                  callback_data='Внести/поменять гос. номер'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("МАКС", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},
     'Зетта Страхование':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {
              'Продление периода': InlineKeyboardButton(
                  text=f'Продление периода {getAmount("Зетта Страхование", "Продление периода")}',
                  callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Зетта Страхование", "Внесение ВУ")}',
                                                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер:': InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                                                       f' {getAmount("Зетта Страхование", "Внести/поменять гос. номер")}',
                                                                  callback_data='Внести/поменять гос. номер'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("Зетта Страхование", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}},
     'Тинькофф Страхование':
         {"alert": "Можно внести только в электронные полиса серии ХХХ",
          "buttons": {
              'Продление периода': InlineKeyboardButton(
                  text=f'Продление периода {getAmount("Тинькофф Страхование", "Продление периода")}',
                  callback_data='Продление периода'),
              'Внесение ВУ': InlineKeyboardButton(
                  text=f'Внесение ВУ {getAmount("Тинькофф Страхование", "Внесение ВУ")}',
                  callback_data='Внесение ВУ'),
              'Внести/поменять гос. номер': InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                                                      f' {getAmount("Тинькофф Страхование", "Внести/поменять гос. номер")}',
                                                                 callback_data='Внести/поменять гос. номер'),
              'Смена собственника': InlineKeyboardButton(
                  text=f'Смена собственника {getAmount("Тинькофф Страхование", "Смена собственника")}',
                  callback_data='Смена собственника'),
              'Исправление ошибки': InlineKeyboardButton(
                  text=f'Исправление ошибки {getAmount("Тинькофф Страхование", "Исправление ошибки")}',
                  callback_data='Исправление ошибки')}}}

buttons_list = \
    {
        'Продление периода': InlineKeyboardButton(text=f'Продление периода',
                                                  callback_data='Продление периода'),
        'Внесение ВУ': InlineKeyboardButton(text=f'Внесение ВУ',
                                            callback_data='Внесение ВУ'),
        'Внести/поменять гос. номер': InlineKeyboardButton(
            text=f'Внести/поменять гос. номер',
            callback_data='Внести/поменять гос. номер'),
        'Смена собственника': InlineKeyboardButton(text=f'Смена собственника',
                                                   callback_data='Смена собственника'),
        'Исправление ошибки': InlineKeyboardButton(text=f'Исправление ошибки',
                                                   callback_data='Исправление ошибки'),
        'Рассторжение полиса': InlineKeyboardButton(
            text=f'Расторжение полиса',
            callback_data='Рассторжение полиса'),
        'Смена цели использования': InlineKeyboardButton(
            text=f'Смена цели использования',
            callback_data='Смена цели использования')
    }

back_button = InlineKeyboardButton(text='Назад', callback_data='Назад')
back_button2 = InlineKeyboardButton(text='Назад', callback_data='Назад2')
back_button3 = InlineKeyboardButton(text='Назад', callback_data='Назад3')
newsk_button = InlineKeyboardButton(text="Выбрать другую СК", callback_data="Выбрать дургую СК")

greet_kb = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton(text='Список доступных СК', callback_data='Список страховых')
button2 = InlineKeyboardButton(text='Тех.поддержка', callback_data='Тех.поддержка.')
button3 = InlineKeyboardButton(text='Сотрудничество с нами', callback_data='Сотрудничество с нами.')
greet_kb.add(button1, button2, button3)

straxkb = InlineKeyboardMarkup(row_width=2)
straxkb.add(*sk_list, newsk_button, back_button)

rosgosstrah_kb = InlineKeyboardMarkup(row_width=1)
rosgosstrah_alert = "Можно внести изменения в любой полис(БСО, еБСО, эл.полис)"
ingosstrah_kb = InlineKeyboardMarkup(row_width=1)
ingosstrah_alert = "Можно внести только в электронные полиса серии ХХХ"
vsk_kb = InlineKeyboardMarkup(row_width=1)
vsk_alert = "Можно внести только в электронные полиса серии ХХХ"
reso_kb = InlineKeyboardMarkup(row_width=1)
reso_alert = "Можно внести изменения в любой полис(БСО, еБСО, эл.полис)"
tinkoff_kb = InlineKeyboardMarkup(row_width=1)
tinkoff_alert = "Можно внести только в электронные полиса серии ХХХ"
sberbank_kb = InlineKeyboardMarkup(row_width=1)
sberbank_alert = "Можно внести только в электронные полиса серии ХХХ"
alfa_kb = InlineKeyboardMarkup(row_width=1)
alfa_alert = "Можно внести только в электронные полиса серии ХХХ"
zetta_kb = InlineKeyboardMarkup(row_width=1)
zetta_alert = "Можно внести только в электронные полиса серии ХХХ"
max_kb = InlineKeyboardMarkup(row_width=1)
max_alert = "Можно внести только в электронные полиса серии ХХХ"
sogaz_kb = InlineKeyboardMarkup(row_width=1)
sogaz_alert = "Изменения вносят на бланки БСО, возможна доставка полисов на любой регион"

sg1 = InlineKeyboardButton(text=f"Продление периода {getAmount('Согаз', 'Продление периода')}",
                           callback_data="Продление периода")
sg2 = InlineKeyboardButton(text=f"Внесение ВУ {getAmount('Согаз', 'Продление периода')}", callback_data="Внесение ВУ")
sg3 = InlineKeyboardButton(text=f"Внести/поменять гос. номер {getAmount('Согаз', 'Внести/поменять гос. номер')}",
                           callback_data="Внести/поменять гос. номер")
sg4 = InlineKeyboardButton(text=f"Смена собственника {getAmount('Согаз', 'Смена собственника')}",
                           callback_data="Смена собственника")
sg5 = InlineKeyboardButton(text=f"Исправление ошибки {getAmount('Согаз', 'Исправление ошибки')}",
                           callback_data="Исправление ошибки")
sogaz_kb.add(sg1, sg2, sg3, sg4, sg5, back_button2)

Ing1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Ингосстрах", "Продление периода")}',
                            callback_data='Продление периода')
Ing2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Ингосстрах", "Внесение ВУ")}', callback_data='Внесение ВУ')
Ing3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер {getAmount("Ингосстрах", "Внести/поменять гос. номер")}',
                            callback_data='Внести/поменять гос. номер')
Ing4 = InlineKeyboardButton(text=f'Смена собственника {getAmount("Ингосстрах", "Смена собственника")}',
                            callback_data='Смена собственника')
Ing5 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Ингосстрах", "Исправление ошибки")}',
                            callback_data='Исправление ошибки')
ingosstrah_kb.add(Ing1, Ing2, Ing3, Ing4, Ing5, back_button2)

vskb1 = InlineKeyboardButton(text=f'Продление периода {getAmount("ВСК", "Продление периода")}',
                             callback_data='Продление периода')
vskb2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("ВСК", "Внесение ВУ")}', callback_data='Внесение ВУ')
vskb3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер {getAmount("ВСК", "Внести/поменять гос. номер")}',
                             callback_data='Внести/поменять гос. номер')
vskb4 = InlineKeyboardButton(text=f'Смена собственника {getAmount("ВСК", "Смена собственника")}',
                             callback_data='Смена собственника')
vskb5 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("ВСК", "Исправление ошибки")}',
                             callback_data='Исправление ошибки')
vskb6 = InlineKeyboardButton(text=f'Рассторжение полиса {getAmount("ВСК", "Рассторжение полиса")}',
                             callback_data='Рассторжение полиса')
vskb7 = InlineKeyboardButton(text=f'Смена цели использования {getAmount("ВСК", "Смена цели использования")}',
                             callback_data='Смена цели использования')
vsk_kb.add(vskb1, vskb2, vskb3, vskb4, vskb5, vskb6, vskb7, back_button2)

rs1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Росгосстрах", "Продление периода")}',
                           callback_data='Продление периода')
rs2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Росгосстрах", "Внесение ВУ")}', callback_data='Внесение ВУ')
rs3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер {getAmount("Росгосстрах", "Внести/поменять гос. номер")}',
                           callback_data='Внести/поменять гос. номер')
rs4 = InlineKeyboardButton(text=f'Смена собственника {getAmount("Росгосстрах", "Смена собственника")}',
                           callback_data='Смена собственника')
rs5 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Росгосстрах", "Исправление ошибки")}',
                           callback_data='Исправление ошибки')
rs6 = InlineKeyboardButton(text=f'Рассторжение полиса {getAmount("Росгосстрах", "Рассторжение полиса")}',
                           callback_data='Рассторжение полиса')
rs7 = InlineKeyboardButton(text=f'Смена цели использования {getAmount("Росгосстрах", "Смена цели использования")}',
                           callback_data='Смена цели использования')
rosgosstrah_kb.add(rs1, rs2, rs3, rs4, rs5, rs6, rs7, back_button2)

alf1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Альфа Страхование", "Продление периода")}',
                            callback_data='Продление периода')
alf2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Альфа Страхование", "Внесение ВУ")}',
                            callback_data='Внесение ВУ')
alf3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер '
                                 f'{getAmount("Альфа Страхование", "Внести/поменять гос. номер")}',
                            callback_data='Внести/поменять гос. номер')
alf4 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Альфа Страхование", "Исправление ошибки")}',
                            callback_data='Исправление ошибки')
alfa_kb.add(alf1, alf2, alf3, alf4, back_button2)

zt1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Зетта Страхование", "Продление периода")}',
                           callback_data='Продление периода')
zt2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Зетта Страхование", "Внесение ВУ")}',
                           callback_data='Внесение ВУ')
zt3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                f' {getAmount("Зетта Страхование", "Внести/поменять гос. номер")}',
                           callback_data='Внести/поменять гос. номер')
zt4 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Зетта Страхование", "Исправление ошибки")}',
                           callback_data='Исправление ошибки')
zetta_kb.add(zt1, zt2, zt3, zt4, back_button2)

res1 = InlineKeyboardButton(text=f'Продление периода {getAmount("РЕСО", "Продление периода")}',
                            callback_data='Продление периода')
res2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("РЕСО", "Внесение ВУ")}',
                            callback_data='Внесение ВУ')
res3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер {getAmount("РЕСО", "Внести/поменять гос. номер")}',
                            callback_data='Внести/поменять гос. номер')
res4 = InlineKeyboardButton(text=f'Смена собственника {getAmount("РЕСО", "Смена собственника")}',
                            callback_data='Смена собственника')
res5 = InlineKeyboardButton(text=f'Смена цели использования {getAmount("РЕСО", "Смена цели использования")}',
                            callback_data='Смена цели использования')
res6 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("РЕСО", "Исправление ошибки")}',
                            callback_data='Исправление ошибки')
reso_kb.add(res1, res2, res3, res4, res5, res6, back_button2)

tin1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Тинькофф Страхование", "Продление периода")}',
                            callback_data='Продление периода')
tin2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Тинькофф Страхование", "Внесение ВУ")}',
                            callback_data='Внесение ВУ')
tin3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                 f' {getAmount("Тинькофф Страхование", "Внести/поменять гос. номер")}',
                            callback_data='Внести/поменять гос. номер')
tin4 = InlineKeyboardButton(text=f'Смена собственника {getAmount("Тинькофф Страхование", "Смена собственника")}',
                            callback_data='Смена собственника')
tin5 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Тинькофф Страхование", "Исправление ошибки")}',
                            callback_data='Исправление ошибки')
tinkoff_kb.add(tin1, tin2, tin3, tin4, tin5, back_button2)

max1 = InlineKeyboardButton(text=f'Продление периода {getAmount("МАКС", "Исправление ошибки")}',
                            callback_data='Продление периода')
max2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("МАКС", "Внесение ВУ")}', callback_data='Внесение ВУ')
max3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер {getAmount("МАКС", "Внести/поменять гос. номер")}',
                            callback_data='Внести/поменять гос. номер')
max4 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("МАКС", "Исправление ошибки")}',
                            callback_data='Исправление ошибки')
max_kb.add(max1, max2, max3, max4, back_button2)

sber1 = InlineKeyboardButton(text=f'Продление периода {getAmount("Сбер Страхование", "Продление периода")}',
                             callback_data='Продление периода')
sber2 = InlineKeyboardButton(text=f'Внесение ВУ {getAmount("Сбер Страхование", "Внесение ВУ")}',
                             callback_data='Внесение ВУ')
sber3 = InlineKeyboardButton(text=f'Внести/поменять гос. номер'
                                  f' {getAmount("Сбер Страхование", "Внести/поменять гос. номер")}',
                             callback_data='Внести/поменять гос. номер')
sber4 = InlineKeyboardButton(text=f'Исправление ошибки {getAmount("Сбер Страхование", "Исправление ошибки")}',
                             callback_data='Исправление ошибки')
sberbank_kb.add(sber1, sber2, sber3, sber4, back_button2)

finish_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
finishButton = KeyboardButton('Завершить отправку файлов')
cancelButton = KeyboardButton("Отмена")
finish_kb.add(finishButton, cancelButton)

payment1500_kb = InlineKeyboardMarkup(row_width=1)
button1500 = InlineKeyboardButton(text="Оплатить 1500₽", callback_data="1500")
payment1500_kb.add(button1500)

payment3000_kb = InlineKeyboardMarkup(row_width=1)
button3000 = InlineKeyboardButton(text="Оплатить 3000₽", callback_data="3000")
payment3000_kb.add(button3000)

payment5000_kb = InlineKeyboardMarkup(row_width=1)
button5000 = InlineKeyboardButton(text="Оплатить 5000₽", callback_data="5000")
payment5000_kb.add(button5000)

check_payment_kb = InlineKeyboardMarkup(row_width=1)
check_payment_button = InlineKeyboardButton(text="Проверить платеж", callback_data="Проверить платеж")
check_payment_kb.add(check_payment_button)

stop_button = InlineKeyboardButton(text="Завершить", callback_data="Завершить")
buttons_kb = InlineKeyboardMarkup(row_width=1)


def optionsValues(sk: str):
    return [keyboards_dict[sk]["buttons"][button] for button in keyboards_dict[sk]["buttons"]]


def buttonsValues():
    return [buttons_list[key] for key in buttons_list]


edit_sk_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Изменить цены", callback_data="Изменить цены"),
    InlineKeyboardButton(text="Изменить название", callback_data="Изменить название"),
    InlineKeyboardButton(text="Изменить всплывающее окно", callback_data="Изменить всплывающее окно"))

admin_panel = InlineKeyboardMarkup(row_width=1)
add_kb_button = InlineKeyboardButton(text="Добавить СК в список", callback_data="Добавить СК в список")
delete_kb_button = InlineKeyboardButton(text="Удалить СК из списка", callback_data="Удалить из списка")
change_options_button = InlineKeyboardButton(text="Изменить опции СК", callback_data="Изменить опции СК")
exit_button = InlineKeyboardButton(text="Выйти из режима панели", callback_data="Выйти из режима панели")

admin_panel.add(add_kb_button, delete_kb_button, change_options_button, exit_button)

sk_dict = {'Внесение ВУ': "Отправьте фото водительского удостоверения с двух сторон (лицевая и оборотная стороны).",
           'Внести/поменять гос. номер': "Отправьте фото СТС (свидетельство о регистрации ТС) с двух сторон (лицевая "
                                         "и оборотная сторона).",
           'Смена собственника': "Отправьте фото СТС (свидетельство о регистрации ТС) и договор купли-продажи с "
                                 "подписями.",
           'Исправление ошибки': "Отправьте фото документов, где указаны верные данные."}
