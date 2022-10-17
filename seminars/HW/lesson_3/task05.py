# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def main(k):
    list_numbers = []
    a, b = 1, 1
    for i in range(k - 1):
        list_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(k):
        list_numbers.insert(0, a)
        a, b = b, a - b

    return list_numbers


if __name__ == "__main__":
    k = int(input('Введите k: '))
    res = main(k)
    print(f'k = {k} -> {res}')
