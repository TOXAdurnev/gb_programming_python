# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


dict_coord = {1: 'x > 0 and y > 0',
              2: 'x < 0 and y > 0',
              3: 'x < 0 and y < 0',
              4: 'x > 0 and y < 0',
              }

quarter = int(input('Введите номер четверти: '))

print(dict_coord[quarter])
