# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def main(list_numbers):
    result = 0
    for i in range(len(list_numbers)):
        if (i % 2) > 0:
            result += list_numbers[i]
    return result


if __name__ == "__main__":
    list_num = [2, 3, 5, 9, 3]
    res = main(list_num)
    print(f'{list_num} -> {res}')
