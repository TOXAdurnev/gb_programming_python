# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def list_prime_factors(number):
    i = 1
    list_result = []
    while i <= number:
        if number % i == 0:
            list_result.append(i)
            number //= i
            i = 2
        else:
            i += 1
    return list_result


if __name__ == "__main__":
    num = int(input('Введите натуральное число N: '))
    res = list_prime_factors(num)
    print(f'Простые множители числа {num} приведены в списке: {res}')
