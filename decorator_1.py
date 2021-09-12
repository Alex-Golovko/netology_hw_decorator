# Домашнее задание к лекции 3.«Decorators»
# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
#
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
#
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.

from _datetime import datetime
import json


def decorator(function):
    def get_info(*args, **kwargs):
        date = datetime.today().replace(microsecond=0)
        new_function = function(*args, **kwargs)
        info = f'Дата и время: {date}, функция: {decorator.__name__}, аргументы: {args}, {kwargs}'
        with open('log.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        print('Данные загружены в файл', 'log.json')
        return new_function
    return get_info


@decorator
def logger(first_name, last_name):
    return first_name, last_name


logger('Вася', 'Пупкин')
