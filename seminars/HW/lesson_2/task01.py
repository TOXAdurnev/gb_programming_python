# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def main(num):
    res = 0
    for i in str(num):
        if i > '0':
            res += int(i)
        else:
            continue
    return res


if __name__ == "__main__":
    number = input('Введите число ')
    result = main(number)
    print(f'{number} -> {result}')
