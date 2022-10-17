# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.python
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def main(n):
    dict_res = {round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)}
    return dict_res


if __name__ == "__main__":
    n = int(input('Введите число '))
    res = main(n)
    print(res)
    print(sum(res))
