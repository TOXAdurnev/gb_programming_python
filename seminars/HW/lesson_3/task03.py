# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def main(list_float):
    list_new = []
    for i in range(len(list_float)):
        fractional_part = list_float[i] % 1
        if fractional_part > 0:
            list_new.append(fractional_part)
        else:
            continue
    result = max(list_new) - min(list_new)
    return result


if __name__ == "__main__":
    list_float = [1.1, 1.2, 3.1, 5, 10.01]
    res = main(list_float)
    print(f'{list_float} -> {round(res, 3)}')
