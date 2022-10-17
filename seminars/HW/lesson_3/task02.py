# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def main(list_numbers):
    result = []
    center_index = (len(list_numbers) - (len(list_numbers) // 2)) - 1
    if len(list_numbers) % 2 == 0:
        counter = -1
        for i in range(center_index + 1):
            start = list_numbers[i]
            end = list_numbers[counter]
            res = start * end
            result.append(res)
            counter -= 1
    else:
        counter = -1
        for i in range(center_index):
            start = list_numbers[i]
            end = list_numbers[counter]
            res = start * end
            result.append(res)
            counter -= 1
        center_res = list_numbers[center_index] ** 2
        result.append(center_res)

    return result


if __name__ == "__main__":
    list_num = [2, 3, 5, 6, 1, 2]
    res = main(list_num)
    print(f'{list_num} -> {res}')
