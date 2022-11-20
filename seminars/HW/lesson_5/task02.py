# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# # чтобы забрать все конфеты у своего конкурента?

from random import randint


def take_players(count_choice_one):
    count_candies_to_take = int(input(f"Введите количество конфет которое возьмете: "))
    if count_candies_to_take > count_choice_one:
        while count_candies_to_take >= count_choice_one:
            count_candies_to_take = int(input(f"Можно брать не больше {count_choice_one} конфет: "))
    return count_candies_to_take


def take_bot(count_choice_one):
    choice = randint(1, count_choice_one)
    print(f'Взял {choice}')
    return choice


def random_player():
    name_player1 = input("Введите имя игрока №1: ")
    name_player2 = input("Введите имя игрока №2: ")
    drawing_queue = randint(0, 2)
    if drawing_queue == 2:
        player1 = name_player2
        player2 = name_player1
    else:
        player1 = name_player1
        player2 = name_player2
    return player1, player2


def random_bot():
    name_bot = 'БОТ'
    name_player1 = input("Ваше имя?")
    drawing_queue = randint(0, 2)
    if drawing_queue == 2:
        player1 = name_bot
        player2 = name_player1
    else:
        player1 = name_player1
        player2 = name_bot
    return player1, player2


def bot_players(name_bot, count_choice_one):
    if name_bot == "БОТ":
        return take_bot(count_choice_one)
    return take_players(count_choice_one)


def name_bot_players(bot_or_player):
    if bot_or_player == 1:
        return random_bot()
    return random_player()


if __name__ == "__main__":
    ########################### идут в функции
    count_candies_all = int(input("Введите количество конфет на столе: "))
    count_choice_one = int(input("Сколько можно брать за раз конфет?: "))
    bot_or_player = int(input("Играем с другом? \n Если с другом введите цифру 0 \n Если с ботом введите цифру 1 \n"))
    name_player1, name_player2 = name_bot_players(bot_or_player)
    k = 0
    while k < count_candies_all:
        print(f'Ход игрока {name_player1}. Осталось {count_candies_all - k} шт')
        move_player1 = bot_players(name_player1, count_choice_one)
        k += move_player1
        if (count_candies_all - k) <= count_choice_one:
            print(f'Выиграл  {name_player2}')
            break
        print(f'Ход игрока {name_player2}. Осталось {count_candies_all - k} шт')
        move_player2 = bot_players(name_player2, count_choice_one)
        k += move_player2
        if (count_candies_all - k) <= count_choice_one:
            print(f'Выиграл {name_player1}')
            break
