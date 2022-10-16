# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def main(n):
    result = []
    for i in range(n):
        number = 1
        for j in range(i + 1):
            number *= (j + 1)
        result.append(number)
    return result


if __name__ == "__main__":
    num = int(input(('Введите число ')))
    res = main(num)
    print(res)
