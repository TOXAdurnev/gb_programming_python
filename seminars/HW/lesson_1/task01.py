# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_weekends(number_day):
    weekends = [6, 7]
    if number_day in weekends:
        res = 'Да'
    else:
        res = 'Нет'
    return f'{number_day} -> {res}'

number_day = int(input('Введите номер дня недели: '))

print(check_weekends(number_day))