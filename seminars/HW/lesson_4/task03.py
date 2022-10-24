# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def drop_duplicates(list_sequence):
    list_result = []
    dict_сount_duplicates = dict((i, list_sequence.count(i)) for i in list_sequence)
    for key, value in dict_сount_duplicates.items():
        if value == 1:
            list_result.append(key)

    return list_result


if __name__ == "__main__":
    list_test = [2, 4, 2, 1]
    res = drop_duplicates(list_test)
    print(f'{list_test} -> {res}')
