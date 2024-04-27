from data_from_json import data
from datetime import datetime


def check_if_executed(data):
    """
    Функция проверяет и выбирает только подходящие операции
    """
    # Создаем список для хранения подходящих словарей
    executed_items = []

    # Перебираем список словарей, начиная с последнего элемента
    for item in reversed(data):
        if item.get('state') == "EXECUTED":
            executed_items.append(item)
        if len(executed_items) == 5:
            break
    return executed_items


# Список подходящих операций
checked_data = check_if_executed(data)


def dicts_corrected(checked_data):
    """
    Исправляет дату в словаре, и из него убирает ненужные данные
    """

    # Тут будут словари с исправленными датами
    updated_data = []

    # Исправляем дату в словарях
    for item in checked_data:
        clear_date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
        input_date = f"{clear_date.day}.{clear_date.month}.{clear_date.year}"
        item['date'] = input_date
        updated_data.append(item)

        # убираем ненужные ключи и значения
        item.pop('state')
        item.pop('id')
    return updated_data


def mask_card_number(sent):
    """
    Маскирует все цифры в номере карты, кроме первых шести и последних четырёх
    """

    # Получаем первые шесть цифр
    first_six = sent[:6]
    # Получаем последние четыре цифры
    last_four = sent[-4:]
    # Маскируем все цифры, кроме первых шести и последних четырех
    middle_masked = "*" * (len(sent) - 10)
    # Формируем маскированное число
    masked_number = first_six + middle_masked + last_four
    # Разбиваем число на блоки по четыре цифры в каждом
    blocks = [masked_number[i:i + 4] for i in range(0, len(masked_number), 4)]
    return blocks


for dictionary in dicts_corrected(checked_data):

    if "from" in dictionary:
        dict_value = dictionary["from"]

    # Разбиваем строку по первому пробелу, ограничиваемся одним разбиением
    parts_of_from = dict_value.split(' ', 1)

    # Берем номер карты отравителя

    sent = parts_of_from[1]

    # Скрываем ненужные цифры
    card_masked = mask_card_number(sent)

    # Преобразовываем данные получателя в необходимый формат
    received = dictionary['to']
    parts_of_to = received.split(' ', 1)
    to = parts_of_to[1]
    new_number = "**" + to[-4:]
    new_to = parts_of_to[0] + ' ' + new_number

    # Объединяем название счета отправителя и уже преобразованный номер карты
    new_from = (str(parts_of_from[0]) + ' ') + ' '.join(card_masked)

    print('')

    # Выводим подготовленные - дату и тип транзакции
    print(dictionary['date'], dictionary["description"])

    # Выводим откуда и кому были переведены деньги
    print(new_from + " -> " + new_to)

    operationAmount = dictionary['operationAmount']['amount']
    operationCurrency = dictionary['operationAmount']['currency']['name']
    print(operationAmount + " " + operationCurrency)
