# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# #
# # Пример:
#
# # - 6782 -> 23
# # - 0,56 -> 11
#
# def main(num):
#     res = 0
#     for i in str(num):
#         if i > '0':
#             res += int(i)
#         else:
#             continue
#     return res
#
#
# if __name__ == "__main__":
#     number = input('Введите число ')
#     result = main(number)
#     print(f'{number} -> {result}')


# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.
result = lambda n: sum(int(d) for d in str(n))
number = 6782
print(f'{number} -> {result(6782)}')
