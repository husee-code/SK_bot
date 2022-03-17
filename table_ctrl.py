#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gspread
import random

gc = gspread.service_account(filename='huy.json')

sh = gc.open("tg_sheet")

worksheet = sh.get_worksheet(0)


def generateOrder():
    column = worksheet.col_values(4)
    while True:
        order = random.randint(100000, 999999)
        if order not in column:
            return order


def payment_table(number):
    new_n = get_line(number)
    worksheet.update_cell(new_n, 8, "Оплачено.")


def update_table(date, s_company, changes, fio, number, user_id, text='Все данные находятся в группе'):
    new_n = len(worksheet.col_values("1")) + 1  # Порядковый номер нового заказа
    worksheet.update_cell(new_n, 1, date)  # Добавляем номер телефона
    worksheet.update_cell(new_n, 2, fio)
    worksheet.update_cell(new_n, 3, number)  # Добавляем номер телефона
    worksheet.update_cell(new_n, 4, generateOrder())  # Добавляем номер заказа
    worksheet.update_cell(new_n, 5, s_company)  # Добавляем название страховой компании
    worksheet.update_cell(new_n, 6, changes)  # Добавляем изменение
    worksheet.update_cell(new_n, 7, text)
    worksheet.update_cell(new_n, 8, "Не оплачено.")
    worksheet.update_cell(new_n, 9, "Не обработано.")
    worksheet.update_cell(new_n, 10, user_id)


def get_line(number: str, answer="line"):
    number = number[1:] if number[0] == "+" else number
    values = worksheet.col_values(3)
    line = len(values) - values[::-1].index(number)
    return line if answer == "line" else worksheet.cell(line, 4).value


def checkPayment():
    for i in range(1, len(worksheet.col_values(1)) + 1):
        values = worksheet.row_values(i)
        if (values[7], values[8]) == ("Оплачено.", "Не обработано."):
            worksheet.update_cell(i, 9, "Обработано.")
            yield values[9], values[3]
