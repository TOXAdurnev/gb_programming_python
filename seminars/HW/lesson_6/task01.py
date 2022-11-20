# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# #
# # Пример:
# #
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
#
# def main(list_numbers):
#     result = 0
#     for i in range(len(list_numbers)):
#         if (i % 2) > 0:
#             result += list_numbers[i]
#     return result
#
#
# if __name__ == "__main__":
#     list_num = [2, 3, 5, 9, 3]
#     res = main(list_num)
#     print(f'{list_num} -> {res}')
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.

def main(list_numbers):
    result = 0
    for i, n in enumerate(list_numbers):
        if (i % 2) > 0:
            result += n
    return result


if __name__ == "__main__":
    list_num = [2, 3, 5, 9, 3]
    res = main(list_num)
    print(f'{list_num} -> {res}')
    #############
    list_num = [2, 3, 5, 9, 3]
    res2 = sum([y for x, y in enumerate(list_num) if x % 2 > 0])
    ##########################################################
