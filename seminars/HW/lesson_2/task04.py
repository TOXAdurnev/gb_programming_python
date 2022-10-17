# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
from random import randint


def create_list(number):
    list_numbers = []
    for i in range(number):
        list_numbers.append(randint(-number, number))
    return list_numbers


def create_txt(number, path):
    with open(path, "w") as file:
        for i in range(number):
            file.write(f'{(randint(-number, number))}\n')


def list_txt(path):
    list_txt = []
    with open(path, "r") as file:
        for line in file:
            list_txt.append(int(line.strip()))
    return list_txt


def product_numbers(position, list_1, list_2):
    number_1 = list_1[position]
    number_2 = list_2[position]
    result = number_1 * number_2
    return result


def mixing_list(list_mine):
    mix_list = list_mine[:]
    list_index = []
    for i in range(len(list_mine)):
        random_number = randint(0, len(list_mine) - 1)
        while random_number in list_index:
            random_number = randint(0, len(list_mine) - 1)
        list_index.append(random_number)
    for i in range(len(list_mine)):
        number = list_mine[list_index[i]]
        mix_list[i] = number

    return mix_list


if __name__ == "__main__":
    path = r'C:/study_analyst_big_data/gb_programming_python/seminars/HW/lesson_2/task04_01.txt'
    num = int(input('Введите число '))
    list_random = create_list(num)
    create_txt(num, path)
    list_txt = list_txt(path)
    pos = randint(0, num - 1)
    res = product_numbers(pos, list_random, list_txt)
    list_mix = mixing_list(list_random)
    print(f'список №1: {list_random} \n'
          f'список №2: {list_txt} \n'
          f'позиция в списках {pos} \n'
          f'произведение чисел из списков ровна: {res}\n'
          f'перемешанный список №1: {list_mix}')
