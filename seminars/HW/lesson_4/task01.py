# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi


def calc_pi(d):
    number_pi = round(pi, d)

    return number_pi


if __name__ == "__main__":
    d = int(input("Введите число точности числа Пи: "))
    number_pi = calc_pi(d)
    print(f'число Пи с заданной точностью {d} равно {number_pi}')
