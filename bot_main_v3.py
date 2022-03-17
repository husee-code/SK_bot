import datetime
import asyncio
import aioschedule
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards_v2 import *
from table_ctrl import *

"ПОШЕЛ НАХУЙ ПИДАРАС 714799964"
token = "token here"
bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

"""У МЕНЯ НЕ БЫЛО ВЫБОРА БЛЯДЬ"""
states = {}
dict_check = {}
back_dict = {}
fio_dict = {}
text_dict = {}
old_message_dict = {}
response_dict = {}
file_dict = {}
photo_dict = {}
cancel_dict = {}
message_id_dict = {}
support_dict = {}
otmena_dict = {}
payment_history_dict = {}
admin_panel_dict = {714799964: {}, 347249536: {}}


def clear_dicts(user_id):
    if user_id in dict_check:
        del dict_check[user_id]
    if user_id in back_dict:
        del back_dict[user_id]
    if user_id in fio_dict:
        del fio_dict[user_id]
    if user_id in text_dict:
        del text_dict[user_id]
    if user_id in old_message_dict:
        del old_message_dict[user_id]
    if user_id in response_dict:
        response_dict[user_id] = []
    if user_id in file_dict:
        del file_dict[user_id]
    if user_id in photo_dict:
        del photo_dict[user_id]
    if user_id in cancel_dict:
        del cancel_dict[user_id]
    if user_id in message_id_dict:
        del message_id_dict[user_id]
    if user_id in otmena_dict:
        otmena_dict[user_id] = 0
    if user_id in support_dict:
        support_dict[user_id] = 0
    states[user_id] = None


""" ЗАПРОС НОМЕРА ЕБАНЫЙ МАШОНКИ """
number_request = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
number_button = KeyboardButton('Оставить номер', request_contact=True)
number_request.add(number_button)


class AdminStates(StatesGroup):
    ADMIN_PANEL_STATE = State()
    USER_STATE = State()


class UserStates(StatesGroup):
    START_STATE = State()
    SK_LIST = State()
    TP_STATE = State()
    OPTIONS_STATE = State()
    ANOTHER_SK_STATE = State()
    GET_FILES_STATE = State()
    GET_FIO_STATE = State()
    GET_MAIN_NUMBER_STATE = State()
    GET_TP_NUMBER_STATE = State()
    GET_NEW_SK_NUMBER_STATE = State()
    PAYMENT_STATE = State()


#  Платежи
async def confirmPayment():
    print("Сработала асинхронная функция!")
    for data in checkPayment():
        print(data)
        await bot.send_message(chat_id=data[0],
                               text=f"Платеж по заказу №{data[1]} подтвержден.\nОператор свяжется с вами в процессе "
                                    f"выполнения заказа.",
                               reply_markup=greet_kb)
        clear_dicts(data[0])
        print("Сработала асинхронная функция! Сообщение отправлено")


"""КЛИЕНТСКАЯ-ХУЕНСКАЯ ЧАСТЬ"""


@dp.message_handler(commands=['start', 'help'], state="*")  # Начало, после кнопки start
async def command_start(message: types.Message):
    await UserStates.START_STATE.set()
    clear_dicts(message.chat.id)
    states[message.chat.id] = None
    await message.answer(greet_text)
    await message.answer(func_txt, reply_markup=greet_kb)
    support_dict[message.chat.id] = 0
    otmena_dict[message.chat.id] = 0
    if message.chat.id not in payment_history_dict:
        payment_history_dict[message.chat.id] = {"active": [], "closed": []}


@dp.message_handler(commands=["open_console"], state="*")  # Открываем консоль
async def openAdminConsole(message: types.Message):
    if message.chat.id in admin_panel_dict:
        await message.answer("Открываем консоль!", reply_markup=admin_panel)
        await AdminStates.ADMIN_PANEL_STATE.set()
        print("Консоль открыта!")
    else:
        await message.answer("Отказано в доступе")
        print("Какого хуя команду спалили")


@dp.message_handler(content_types=("photo", "text", "document"), state=UserStates.GET_FILES_STATE)
async def getFiles(message: types.Message):
    # Получение файлов
    if message.text is not None:
        print("заебись")

        text_dict[message.chat.id] = message.text

    if message.document is not None:
        if message.chat.id not in file_dict:
            file_dict[message.chat.id] = [message.document["file_id"]]
        else:
            file_dict[message.chat.id].append(message.document["file_id"])

    if message.photo:
        if message.chat.id not in photo_dict:

            photo_dict[message.chat.id] = [message.photo[-1].file_id]
        else:
            photo_dict[message.chat.id].append(message.photo[-1].file_id)

    # Завершить отправку файлов
    if message.text == 'Завершить отправку файлов':
        if message.chat.id not in file_dict and message.chat.id not in photo_dict:  # Проверяем, отправлены ли файлы
            await message.answer("Вы не отправили необходимые данные!")
        else:
            await message.answer(text="Введите ваше ФИО:")  # Переходим на уровень ввода ФИО
            await UserStates.GET_FIO_STATE.set()

    # Отмена
    elif message.text == "Отмена":
        # Очищаем словари от отправленных файлов
        if message.chat.id in file_dict:
            del file_dict[message.chat.id]
        if message.chat.id in photo_dict:
            del photo_dict[message.chat.id]
        response_dict[message.chat.id].pop(len(response_dict[message.chat.id]) - 1)
        await cancel_dict[message.chat.id].answer('Список доступных изменений:',
                                                  reply_markup=InlineKeyboardMarkup(row_width=2).add(
                                                      *optionsValues(response_dict[message.chat.id][0]), back_button2))


@dp.message_handler(content_types="text", state=UserStates.GET_FIO_STATE)
async def getFio(message: types.Message):
    response_dict[message.chat.id].append(message.text)
    await message.answer('Нажмите на кнопку "отправить номер телефона"', reply_markup=number_request)
    await UserStates.GET_MAIN_NUMBER_STATE.set()


@dp.message_handler(content_types=("photo", "text", "document"), state=States.USER_STATE)
async def echo_send(message: types.Message):
    if message.chat.id in dict_check and dict_check[message.chat.id] == 1 \
            and message.text != 'Отмена' and message.text != 'Завершить отправку файлов':
        if message.text is not None:
            print("заебись")

            text_dict[message.chat.id] = message.text

        if message.document is not None:
            if message.chat.id not in file_dict:
                file_dict[message.chat.id] = [message.document["file_id"]]
            else:
                file_dict[message.chat.id].append(message.document["file_id"])

        if message.photo:
            if message.chat.id not in photo_dict:

                photo_dict[message.chat.id] = [message.photo[-1].file_id]
            else:
                photo_dict[message.chat.id].append(message.photo[-1].file_id)

        old_message_dict[message.chat.id] = message.text
        print(dict_check[message.chat.id])

    if message.text == 'Завершить отправку файлов' and not states[message.chat.id]:
        if message.chat.id not in file_dict and message.chat.id not in photo_dict:
            await message.answer("Вы не отправили необходимые данные!")
        else:
            await message.answer(text="Введите ваше ФИО:")
            dict_check[message.chat.id] = 2
    elif message.text == "Отмена":
        if message.chat.id in file_dict:
            del file_dict[message.chat.id]
        if message.chat.id in photo_dict:
            del photo_dict[message.chat.id]
        otmena_dict[message.chat.id] += 2
        response_dict[message.chat.id].pop(len(response_dict[message.chat.id]) - 1)
        await cancel_dict[message.chat.id].answer('Список доступных изменений:',
                                                  reply_markup=InlineKeyboardMarkup(row_width=2).add(
                                                      *optionsValues(response_dict[message.chat.id][0]), back_button2))

    # Это если не нашел нужную СК
    if states[message.chat.id] == "sk":
        response_dict[message.chat.id] = [message.text]
        old_message_dict[message.chat.id] = message.text
        await message.answer("Введите изменения, которые хотите внести в Ваш полис.")
        states[message.chat.id] = "changes"  # переходим на уровень ввода изменения
    elif states[message.chat.id] == "changes" and message.text != old_message_dict[message.chat.id]:
        response_dict[message.chat.id].append(message.text)
        old_message_dict[message.chat.id] = message.text
        await message.answer("Отправьте необходимые документы.", reply_markup=finish_kb)
        states[message.chat.id] = "documents"  # переходим на уровень отправки документов.
    elif states[message.chat.id] == "documents" and message.text != "Завершить отправку файлов" and message.text != \
            old_message_dict[message.chat.id]:
        if message.text is not None:
            text_dict[message.chat.id] = message.text

        if message.document is not None:
            if message.chat.id not in file_dict:
                file_dict[message.chat.id] = [message.document["file_id"]]
            else:
                file_dict[message.chat.id].append(message.document["file_id"])

        if message.photo:
            if message.chat.id not in photo_dict:

                photo_dict[message.chat.id] = [message.photo[-1].file_id]
            else:
                photo_dict[message.chat.id].append(message.photo[-1].file_id)
        old_message_dict[message.chat.id] = message.text

    elif states[message.chat.id] == "documents" and message.text == "Завершить отправку файлов":
        states[message.chat.id] = "fio"  # переходим на уровень ввода фио
        await message.answer('Введите ФИО:')
    elif states[message.chat.id] == "fio" and message.text != "Завершить отправку файлов":
        response_dict[message.chat.id].append(message.text)
        states[message.chat.id] = "send_number"
        await message.answer('Нажмите на кнопку "отправить номер телефона"', reply_markup=number_request)

    # dict_check(id) == 2 -- после нажатия на кнопку "завершить отправку файлов", получаем ФИО
    if message.chat.id in dict_check and (
            message.chat.id not in old_message_dict or old_message_dict[message.chat.id] != message.text) and \
            dict_check[message.chat.id] == 2 and message.text != 'Завершить отправку файлов':
        print('ХУЙЛО ЕБАНОЕ')
        fio_dict[message.chat.id] = message.text

        response_dict[message.chat.id].append(message.text)
        dict_check[message.chat.id] = 3  # ввод номера телефона
        old_message_dict[message.chat.id] = message.text
    if message.chat.id in dict_check and dict_check[message.chat.id] == 3 and states[message.chat.id] != "payment":
        await message.answer(
            text="Нажмите на кнопку 'Оставить номер'. С вами свяжется оператор после оформления заявки.",
            reply_markup=number_request)
    if states[message.chat.id] == "payment":
        if message.photo:
            await bot.send_photo(chat_id=-696978000, photo=message.photo[-1].file_id,
                                 caption=f"{response_dict[message.chat.id][2]}\n"
                                         f"Оплата заказа №  {get_line(response_dict[message.chat.id][3], answer='order')}")
            await message.answer(text="Спасибо! Ожидайте ответа.")


# Получаем контакт после стандартного прохода
@dp.message_handler(content_types=['contact'], state=UserStates.GET_MAIN_NUMBER_STATE)
async def getContactMain(number: types.Contact):
    await bot.send_message(text="⏳", chat_id=number["from"]["id"], reply_markup=types.ReplyKeyboardRemove())
    response_dict[number["from"]["id"]].append(number["contact"]["phone_number"])
    # Отгружаем файлы в чат
    if number["from"]["id"] in text_dict:
        update_table(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), *response_dict[number["from"]["id"]],
                     number["from"]["id"], text_dict[number["from"]["id"]])
    else:
        update_table(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), *response_dict[number["from"]["id"]],
                     number["from"]["id"])

    if number["from"]["id"] in photo_dict:
        if len(photo_dict[number["from"]["id"]]):
            for ph in photo_dict[number["from"]["id"]]:
                await bot.send_photo(chat_id=-696978000, photo=ph,
                                     caption=f"{response_dict[number['from']['id']][2]}\n"
                                             f"Номер заказа: {get_line(str(number['contact']['phone_number']), answer='order')}")
    if number["from"]["id"] in file_dict:
        if len(file_dict[number["from"]["id"]]):
            for file in file_dict[number["from"]["id"]]:
                await bot.send_document(chat_id=-696978000, document=file,
                                        caption=f"{response_dict[number['from']['id']][2]}\n"
                                                f"Номер заказа: {get_line(str(number['contact']['phone_number']), answer='order')}")

    # Отправляем сообщение об оплате
    await bot.send_message(chat_id=number["from"]["id"],
                           text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                "благотворительности. В дальнейшем этот номер будет использован как нашими операторами "
                                "в процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                "заказом.")
    await bot.send_message(chat_id=number["from"]["id"],
                           text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                f'+///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\n'
                                f'Сумма для перевода: '
                                f"{getAmount(response_dict[number['from']['id']][0], response_dict[number['from']['id']][1])}р."
                                f"\nПосле оплаты, отправьте, пожалуйста чек:")
    states[number["from"]["id"]] = "payment"
    await UserStates.PAYMENT_STATE.set()


# Получаем контакт из запроса на техподдержку
@dp.message_handler(content_types=['contact'], state=UserStates.GET_TP_NUMBER_STATE)
async def getTPContact(number: types.Contact):
    await bot.send_message(text="⏳", chat_id=number["from"]["id"], reply_markup=types.ReplyKeyboardRemove())
    if "username" in number["from"]:
        await bot.send_message(chat_id=-696978000,
                               text=f'Оставлена заявка на техподдержку. Ссылка: @{number["from"]["username"]}\n'
                                    f'Номер: {number["contact"]["phone_number"]}')
        await cancel_dict[number["from"]["id"]].answer(text="Заявка принята. Ожидайте ответа.", show_alert=True)
        await cancel_dict[number["from"]["id"]].message.answer(text="Заявка принята. Ожидайте ответа.",
                                                               reply_markup=types.ReplyKeyboardRemove())
        await cancel_dict[number["from"]["id"]].message.answer(text=func_txt, reply_markup=greet_kb)
    else:
        await bot.send_message(chat_id=-696978000,
                               text=f'Оставлена заявка на техподдержку. Ссылка на акканут отсутствует.\n'
                                    f'Номер: {number["contact"]["phone_number"]}')
        await cancel_dict[number["from"]["id"]].answer(text="Заявка принята. Ожидайте ответа.", show_alert=True)
        await cancel_dict[number["from"]["id"]].message.answer(text="Заявка принята. Ожидайте ответа.",
                                                               reply_markup=types.ReplyKeyboardRemove())
        await cancel_dict[number["from"]["id"]].message.answer(text=func_txt,
                                                               reply_markup=types.ReplyKeyboardRemove())

    del cancel_dict[number["from"]["id"]]
    dict_check[number["from"]["id"]] = 0


@dp.message_handler(content_types=['contact'], state=UserStates.GET_MAIN_NUMBER_STATE)
async def get_contact(number: types.contact):
    await bot.send_message(text="⏳", chat_id=number["from"]["id"], reply_markup=types.ReplyKeyboardRemove())
    if number["from"]["id"] in dict_check and dict_check[number["from"]["id"]] == 4:  # 4 уровень -- техподдержка
        if "username" in number["from"]:
            await bot.send_message(chat_id=-696978000,
                                   text=f'Оставлена заявка на техподдержку. Ссылка: @{number["from"]["username"]}\n'
                                        f'Номер: {number["contact"]["phone_number"]}')
            await cancel_dict[number["from"]["id"]].answer(text="Заявка принята. Ожидайте ответа.", show_alert=True)
            await cancel_dict[number["from"]["id"]].message.answer(text="Заявка принята. Ожидайте ответа.",
                                                                   reply_markup=types.ReplyKeyboardRemove())
            await cancel_dict[number["from"]["id"]].message.answer(text=func_txt, reply_markup=greet_kb)
        else:
            await bot.send_message(chat_id=-696978000,
                                   text=f'Оставлена заявка на техподдержку. Ссылка на акканут отсутствует.\n'
                                        f'Номер: {number["contact"]["phone_number"]}')
            await cancel_dict[number["from"]["id"]].answer(text="Заявка принята. Ожидайте ответа.", show_alert=True)
            await cancel_dict[number["from"]["id"]].message.answer(text="Заявка принята. Ожидайте ответа.",
                                                                   reply_markup=types.ReplyKeyboardRemove())
            await cancel_dict[number["from"]["id"]].message.answer(text=func_txt,
                                                                   reply_markup=types.ReplyKeyboardRemove())

        del cancel_dict[number["from"]["id"]]
        dict_check[number["from"]["id"]] = 0
    else:

        response_dict[number["from"]["id"]].append(number["contact"]["phone_number"])
        if number["from"]["id"] in text_dict:
            update_table(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), *response_dict[number["from"]["id"]],
                         number["from"]["id"], text_dict[number["from"]["id"]])
        else:
            update_table(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"), *response_dict[number["from"]["id"]],
                         number["from"]["id"])

        if number["from"]["id"] in photo_dict:
            if len(photo_dict[number["from"]["id"]]):
                for ph in photo_dict[number["from"]["id"]]:
                    await bot.send_photo(chat_id=-696978000, photo=ph,
                                         caption=f"{response_dict[number['from']['id']][2]}\n"
                                                 f"Номер заказа: {get_line(str(number['contact']['phone_number']), answer='order')}")
        if number["from"]["id"] in file_dict:
            if len(file_dict[number["from"]["id"]]):
                for file in file_dict[number["from"]["id"]]:
                    await bot.send_document(chat_id=-696978000, document=file,
                                            caption=f"{response_dict[number['from']['id']][2]}\n"
                                                    f"Номер заказа: {get_line(str(number['contact']['phone_number']), answer='order')}")

        if response_dict[number["from"]["id"]][0] == "ВСК" \
                or response_dict[number["from"]["id"]][0] == 'Альфа Страхование' \
                or response_dict[number["from"]["id"]][0] == 'Зетта Страхование' \
                or response_dict[number["from"]["id"]][0] == 'Тинькофф Страхование' \
                or response_dict[number["from"]["id"]][0] == 'МАКС' \
                or response_dict[number["from"]["id"]][0] == 'Сбер Страхование':
            # await bot.send_message(text="История платежей", chat_id=number["from"]["id"], reply_markup=payment1500_kb)

            await bot.send_message(chat_id=number["from"]["id"],
                                   text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                        "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                        "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                        "благотворительности. В дальнейшем этот номер будет использован как нашими операторами в "
                                        "процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                        "заказом.")
            await bot.send_message(chat_id=number["from"]["id"],
                                   text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                        f'///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\nСумма для перев'
                                        f"ода: 1500р.\nПосле оплаты, отправьте, пожалуйста чек:")
            states[number["from"]["id"]] = "payment"

        elif response_dict[number["from"]["id"]][0] == "Ингосстрах":

            await bot.send_message(chat_id=number["from"]["id"],
                                   text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                        "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                        "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                        "благотворительности. В дальнейшем этот номер будет использован как нашими операторами в "
                                        "процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                        "заказом.")
            await bot.send_message(chat_id=number["from"]["id"],
                                   text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                        f'///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\nСумма для перев'
                                        f"ода: 2000р.\nПосле оплаты, отправьте, пожалуйста чек:")
            states[number["from"]["id"]] = "payment"

        elif response_dict[number["from"]["id"]][0] == 'Росгосстрах' \
                or response_dict[number["from"]["id"]][0] == 'Согаз':
            # await bot.send_message(text="История платежей", chat_id=number["from"]["id"], reply_markup=payment3000_kb)
            await bot.send_message(chat_id=number["from"]["id"],
                                   text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                        "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                        "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                        "благотворительности. В дальнейшем этот номер будет использован как нашими операторами в "
                                        "процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                        "заказом.")
            await bot.send_message(chat_id=number["from"]["id"],
                                   text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                        f'///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\nСумма для перев'
                                        f"ода: 3000р.\nПосле оплаты, отправьте, пожалуйста чек:")
            states[number["from"]["id"]] = "payment"
        elif response_dict[number["from"]["id"]][0] == 'РЕСО':
            if response_dict[number["from"]["id"]][1] == "Смена собственника" \
                    or response_dict[number["from"]["id"]][1] == "Смена Цели использования":
                # await bot.send_message(text="История платежей", chat_id=number["from"]["id"], reply_markup=payment5000_kb)
                await bot.send_message(chat_id=number["from"]["id"],
                                       text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                            "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                            "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                            "благотворительности. В дальнейшем этот номер будет использован как нашими операторами в "
                                            "процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                            "заказом.")
                await bot.send_message(chat_id=number["from"]["id"],
                                       text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                            f'///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\nСумма для перев'
                                            f"ода: 5000р.\nПосле оплаты, отправьте, пожалуйста чек:")
                states[number["from"]["id"]] = "payment"
            else:
                # await bot.send_message(text="История платежей", chat_id=number["from"]["id"], reply_markup=payment3000_kb)
                await bot.send_message(chat_id=number["from"]["id"],
                                       text="Для того, чтобы ваш заказ был запущен в работу, его нужно оплатить. На данный момент "
                                            "оплата происходит на карту сбербанка. Внимание! ОБЯЗАТЕЛЬНО указывать в комментарии к "
                                            "переводу порядковый номер вашего заказа. Отправления без номера приравниваются к "
                                            "благотворительности. В дальнейшем этот номер будет использован как нашими операторами в "
                                            "процессе работы, так и вами для обращения к сервису по вопросам, связанными с вашим "
                                            "заказом.")
                await bot.send_message(chat_id=number["from"]["id"],
                                       text=f"Номер карты (Сбербанк): ///\nНомер для перевода (Сбербанк): "
                                            f'///\nНомер вашего заказа: {get_line(number["contact"]["phone_number"], answer="order")}\nСумма для перев'
                                            f"ода: 3000р.\nПосле оплаты, отправьте, пожалуйста чек:")
                states[number["from"]["id"]] = "payment"


@dp.callback_query_handler(
    text=['Список страховых', 'Тех.поддержка.', 'Сотрудничество с нами.', 'Назад3'],
    state="*")  # Второй этап. greet_kb
async def start(callback: types.CallbackQuery):
    if callback.data == 'Список страховых':
        await callback.message.edit_text('Выбрать СК:', reply_markup=InlineKeyboardMarkup(row_width=2).add(*sk_list))
        await UserStates.SK_LIST.set()
    elif callback.data == 'Тех.поддержка.':
        dict_check[callback.message.chat.id] = 4
        support_dict[callback.message.chat.id] = 1
        cancel_dict[callback.message.chat.id] = callback  # сохраняем callback
        await callback.message.answer('Оставьте свой номер телефона, с вами свяжутся.', reply_markup=number_request)
        await UserStates.TP_STATE.set()
    elif callback.data == 'Назад3':
        await callback.message.edit_text(func_txt, reply_markup=greet_kb)
        await UserStates.START_STATE.set()

    elif callback.data == 'Сотрудничество с нами.':
        await callback.message.edit_text("Наши контакты: "
                                         "/// - пишите в WhatsApp",
                                         reply_markup=InlineKeyboardMarkup(row_width=1).add(back_button))


@dp.callback_query_handler(state=UserStates.SK_LIST)  # 3 этап. Выбор СК
async def sk_type(callback: types.CallbackQuery):
    response_dict[callback.message.chat.id] = [callback.data]
    print(response_dict)
    if callback.data not in ["Назад", "Назад2"]:
        await UserStates.OPTIONS_STATE.set()
        await callback.message.edit_text('Список доступных изменений:',
                                         reply_markup=InlineKeyboardMarkup(row_width=1).add(*optionsValues(callback.data),
                                                                                            back_button2))
        await callback.answer(text=keyboards_dict[callback.data]["alert"], show_alert=True)
    if callback.data == "Выбрать дургую СК":
        await UserStates.ANOTHER_SK_STATE.set()
        states[callback.message.chat.id] = "sk"  # переходим на уровень ввода СК
        file_dict[callback.message.chat.id] = []
        photo_dict[callback.message.chat.id] = []
        await callback.answer(text="Предоплата услуги 1500 рублей, возможен перерасчет в зависимости от"
                                   "указанной вами услугой.  В случае отказа с нашей"
                                   " стороны, денежные средства будут возвращены")
        await callback.message.answer("Введите СК:")
    elif callback.data == "Назад":
        await UserStates.START_STATE.set()  # Возвращаемся в начало
        await callback.message.edit_text(func_txt, reply_markup=greet_kb)
    cancel_dict[callback.message.chat.id] = callback.message


@dp.callback_query_handler(state=UserStates.OPTIONS_STATE)  # Проверяем выбранную опцию
async def chooseOption(option: types.CallbackQuery):
    if option.data == "Назад2":
        await option.message.edit_text("Выбрать СК:", reply_markup=InlineKeyboardMarkup(row_width=2).add(*sk_list))
        await UserStates.SK_LIST.set()
    elif option.data != 'Назад2':
        response_dict[option.message.chat.id].append(option.data)
        await option.message.delete_reply_markup()
        await option.message.edit_text(func_txt)
        dict_check[option.message.chat.id] = 1

        if option.data == 'Внесение ВУ':
            await option.message.answer(
                text='При внесении водителей может потребоваться перерасчёт по полису. '
                     'В случае необходимости доплаты, наш оператор свяжется с вами и пришлёт вам ссылку на оплату. '
                     'В случае, если сумма полиса уменьшается, оператор запросит у вас реквизиты для возврата '
                     'разницы от страховой компании.')

        if option.data in sk_dict:
            await option.message.answer(
                text="Обязательно отправьте фото/pdf файл страхового полиса, фото паспорта страхователя "
                     "(главная страница и страница с пропиской)." + "\n" + sk_dict[option.data],
                reply_markup=finish_kb)
        else:
            await option.message.answer(
                text="Обязательно отправьте фото/pdf файл страхового полиса, фото паспорта страхователя "
                     "(главная страница и страница с пропиской).",
                reply_markup=finish_kb)
        await UserStates.GET_FILES_STATE.set()


"ПОШЕЛ НАХУЙ ПИДАРАС"


@dp.message_handler(state=AdminStates.ADMIN_PANEL_STATE)
async def adminCheckMessage(message: types.Message):
    print("готово")
    # Функционал админ панельки
    if message.chat.id in admin_panel_dict:
        if admin_panel_dict[message.chat.id]["states"] == "Добавить СК в список":
            admin_panel_dict[message.chat.id]["new_sk"] = message.text
            sk_list.append(InlineKeyboardButton(text=message.text, callback_data=message.text))
            keyboards_dict[message.text] = {"alert": None, "buttons": {}}
            prices_dict[message.text] = {}
            admin_panel_dict[message.chat.id]["states"] = "get alert"
            await message.answer(text="Введите, какие документы необходимы. Примеры:\n"
                                      "'Можно внести изменения в любой полис(БСО, еБСО, эл.полис)'\n"
                                      "'Можно внести только в электронные полиса серии ХХХ'")

        elif admin_panel_dict[message.chat.id]["states"] == "Выбор кнопки" and message.text != \
                admin_panel_dict[message.chat.id]["new_sk"]:
            admin_panel_dict[message.chat.id]["button_price"] = message.text[message.text.index("*") + 1:len(
                message.text) - message.text[::-1].index("*") - 1]  # Даже не спрашивай что это за хуйня
            prices_dict[admin_panel_dict[message.chat.id]["new_sk"]][
                message.text[:message.text.index('*')]] = message.text[
                                                          message.text.index("*") + 1:len(message.text) - message.text[
                                                                                                          ::-1].index(
                                                              "*") - 1]  # та же залупа
            admin_panel_dict[message.chat.id]["new_button"] = message.text[:message.text.index('*')]
            buttons_list[message.text[:message.text.index("*")]] = InlineKeyboardButton(
                text=message.text[:message.text.index("*")], callback_data=message.text[:message.text.index("*")])
            keyboards_dict[admin_panel_dict[message.chat.id]["new_sk"]]["buttons"][
                admin_panel_dict[message.chat.id]["new_button"]] = InlineKeyboardButton(
                text=message.text[:message.text.index("*")] +
                     f" {getAmount(admin_panel_dict[message.chat.id]['new_sk'], message.text[:message.text.index('*')])}",
                callback_data=message.text[:message.text.index("*")])
        elif admin_panel_dict[message.chat.id]["states"] == "get amount":
            prices_dict[admin_panel_dict[message.chat.id]["new_sk"]][
                admin_panel_dict[message.chat.id]["callback"].data] = message.text
            # в данном случае callback -- выбранная кнопка
            print(admin_panel_dict[message.chat.id]['callback'].data)

            keyboards_dict[admin_panel_dict[message.chat.id]["new_sk"]]["buttons"][
                admin_panel_dict[message.chat.id]["callback"].data] = InlineKeyboardButton(
                text=admin_panel_dict[message.chat.id][
                         "callback"].data + f" {getAmount(admin_panel_dict[message.chat.id]['new_sk'], admin_panel_dict[message.chat.id]['callback'].data)}",
                callback_data=admin_panel_dict[message.chat.id]['callback'].data)

            admin_panel_dict[message.chat.id]["states"] = "Выбор кнопки"
        elif admin_panel_dict[message.chat.id]["states"] == "get alert":
            keyboards_dict[admin_panel_dict[message.chat.id]["new_sk"]][
                "alert"] = message.text

            await message.answer("Выберите кнопки, которые хотите добавить. \n"
                                 "Если нужной кнопки нет в списке, введите ее название и стоимость услуги,"
                                 "выделив их символами *\n"
                                 "Пример: Кнопка 1 *1500*",
                                 reply_markup=InlineKeyboardMarkup(row_width=1).add(*buttonsValues(),
                                                                                    stop_button))  # Выводим все существующие кнопки для изменений.
            admin_panel_dict[message.chat.id]["states"] = "Выбор кнопки"
        elif admin_panel_dict[message.chat.id]["states"] == "edit_sk_alert":
            keyboards_dict[admin_panel_dict[message.chat.id]["sk"]]["alert"] = message.text
            await message.answer(text="список функций", reply_markup=admin_panel)
            admin_panel_dict[message.chat.id]["states"] = "choose_sk"
        elif admin_panel_dict[message.chat.id]["states"] == "edit_button_price":
            prices_dict[admin_panel_dict[message.chat.id]["sk"]][
                admin_panel_dict[message.chat.id]["button"]] = message.text
            keyboards_dict[admin_panel_dict[message.chat.id]["sk"]]["buttons"][
                admin_panel_dict[message.chat.id]["button"]] = InlineKeyboardButton(
                text=f'{admin_panel_dict[message.chat.id]["button"]} {getAmount(admin_panel_dict[message.chat.id]["sk"], admin_panel_dict[message.chat.id]["button"])}',
                callback_data=admin_panel_dict[message.chat.id]["button"])
            await message.answer("Готово!", reply_markup=admin_panel)
        elif admin_panel_dict[message.chat.id]["states"] == "edit_button":
            prices_dict[admin_panel_dict[message.chat.id]["sk"]][message.text] = getAmount(
                admin_panel_dict[message.chat.id]["sk"], admin_panel_dict[message.chat.id]["button"])[2:]
            del prices_dict[admin_panel_dict[message.chat.id]["sk"]][admin_panel_dict[message.chat.id]["button"]]
            del keyboards_dict[admin_panel_dict[message.chat.id]["sk"]]["buttons"][
                admin_panel_dict[message.chat.id]["button"]]

            keyboards_dict[admin_panel_dict[message.chat.id]["sk"]]["buttons"][message.text] = \
                InlineKeyboardButton(
                    text=f'{message.text} {getAmount(admin_panel_dict[message.chat.id]["sk"], message.text)}',
                    callback_data=message.text)
            await message.answer("Готово!", reply_markup=admin_panel)


@dp.callback_query_handler(state=States.ADMIN_PANEL_STATE)
async def checkAdminCallback(callback: types.CallbackQuery):
    print("готово")
    if callback.data == "Добавить СК в список":
        await callback.message.answer("Введите название СК")
        admin_panel_dict[callback.message.chat.id]["states"] = "Добавить СК в список"
    elif callback.data == "Удалить из списка":
        await callback.message.answer("Выберите СК, которую хотите удалить из списка",
                                      reply_markup=InlineKeyboardMarkup(row_width=1).add(*sk_list))
        admin_panel_dict[callback.message.chat.id]["states"] = "Удалить из списка"
    elif callback.data == "Изменить опции СК":
        await callback.message.answer("Выберите СК, опции которой хотите изменить",
                                      reply_markup=InlineKeyboardMarkup(row_width=2).add(*sk_list))
        admin_panel_dict[callback.message.chat.id]["states"] = "Изменить опции СК"
    elif callback.data == "Удалить из списка":
        del sk_list[callback.data]
        del keyboards_dict[callback.data]
    elif callback.data == "Выйти из режима панели":
        print(555)
        clear_dicts(callback.message.chat.id)
        states[callback.message.chat.id] = None
        await callback.message.answer(greet_text)
        await callback.message.answer(func_txt, reply_markup=greet_kb)
        support_dict[callback.message.chat.id] = 0
        otmena_dict[callback.message.chat.id] = 0
        await States.USER_STATE.set()

    # Выбор кнопок
    elif admin_panel_dict[callback.message.chat.id]["states"] == "Выбор кнопки" and callback.data != "Завершить":
        if buttons_list[callback.data] not in \
                keyboards_dict[admin_panel_dict[callback.message.chat.id]["new_sk"]]["buttons"]:
            await callback.message.answer("Введите стоимость данной услуги")
            admin_panel_dict[callback.message.chat.id]["states"] = "get amount"
            admin_panel_dict[callback.message.chat.id][
                "callback"] = callback  # в данном случае callback -- выбранная кнопка
        else:
            await callback.message.answer("Эта кнопка уже присутствует")
    elif admin_panel_dict[callback.message.chat.id]["states"] == "Выбор кнопки" and callback.data == "Завершить":
        await callback.message.answer(text="Открываем консоль!",
                                      reply_markup=admin_panel)
        admin_panel_dict[callback.message.chat.id]["states"] = "option"
    elif admin_panel_dict[callback.message.chat.id]["states"] == "option" and callback.data != "Завершить":
        # Создаем клавиатуру опций СК
        await callback.message.answer(text="text",
                                      reply_markup=InlineKeyboardMarkup(row_width=1).add(*optionsValues(callback.data),
                                                                                         back_button2))
        await callback.answer(text=keyboards_dict[callback.data]["alert"], show_alert=True)

    # Изменение существующей СК
    elif admin_panel_dict[callback.message.chat.id][
        "states"] == "Изменить опции СК" and callback.data != "Изменить опции СК":
        await callback.message.answer(text="Выберите нужную опцию", reply_markup=edit_sk_kb)
        admin_panel_dict[callback.message.chat.id]["states"] = "edit_sk_kb"
        admin_panel_dict[callback.message.chat.id]["sk"] = callback.data
    elif admin_panel_dict[callback.message.chat.id]["states"] == "edit_sk_kb" and callback.data == "Изменить цены":
        admin_panel_dict[callback.message.chat.id]["states"] = "edit_button_price"
        await callback.message.edit_text(text=f"Доступные изменения в '{callback.data}'",
                                         reply_markup=InlineKeyboardMarkup(row_width=1).add(
                                             *optionsValues(admin_panel_dict[callback.message.chat.id]["sk"])))
    elif admin_panel_dict[callback.message.chat.id]["states"] == "edit_sk_kb" and callback.data == "Изменить название":
        admin_panel_dict[callback.message.chat.id]["states"] = "edit_button"
        await callback.message.edit_text(text=f"Доступные изменения в '{callback.data}'",
                                         reply_markup=InlineKeyboardMarkup(row_width=1).add(
                                             *optionsValues(admin_panel_dict[callback.message.chat.id]["sk"])))

    # меняем кнопки
    elif admin_panel_dict[callback.message.chat.id][
        "states"] == "edit_button_price" and callback.data != "Изменить цены":
        admin_panel_dict[callback.message.chat.id]["button"] = callback.data
        await callback.message.answer("Введите новую стоимость этой опции")
    elif admin_panel_dict[callback.message.chat.id]["states"] == "edit_button" and callback.data != "Изменить название":
        admin_panel_dict[callback.message.chat.id]["button"] = callback.data
        await callback.message.answer("Введите новое название этой опции")
    elif admin_panel_dict[callback.message.chat.id][
        "states"] == "edit_sk_kb" and callback.data == "Изменить всплывающее окно":
        await callback.message.answer(text="Введите, какие документы необходимы для этой СК")
        admin_panel_dict[callback.message.chat.id]["states"] = "edit_sk_alert"
    elif admin_panel_dict[callback.message.chat.id]["states"] == "choose_sk":
        await callback.message.answer(text="Список изменений",
                                      reply_markup=InlineKeyboardMarkup(row_width=1).add(*optionsValues(callback.data),
                                                                                         back_button2))
        await callback.answer(text=keyboards_dict[callback.data]["alert"], show_alert=True)


async def scheduler():
    aioschedule.every(1).minutes.do(confirmPayment)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    asyncio.create_task(scheduler())


executor.start_polling(dispatcher=dp, on_startup=on_startup)
