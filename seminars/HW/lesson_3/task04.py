# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def main(number):
    result = ''
    while number != 0:
        result = str(number % 2) + result
        number //= 2
    return result


if __name__ == "__main__":
    num = int(input('Введите десятичное число для перевода в двоичное: '))
    res = main(num)
    print(f'{num} -> {res}')
