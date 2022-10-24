# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools


def get_ratios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)

    return ratios


def get_polynomial(k, ratios):
    var = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'

    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


if __name__ == "__main__":
    k = randint(2, 7)
    ratios = get_ratios(k)
    res = get_polynomial(k, ratios)
    print(f'k = {k} -> {res}')
    with open('Polynomial.txt', 'w') as data:
        data.write(res)
    ## для task05
    k = randint(2, 8)
    ratios = get_ratios(k)
    res = get_polynomial(k, ratios)
    print(f'k = {k} -> {res}')
    with open('Polynomial2.txt', 'w') as data:
        data.write(res)
