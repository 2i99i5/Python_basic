"""
Создайте программу для игры с конфетами человек против компьютера.
Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем
28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Подумайте как наделить бота "интеллектом"
"""
"""
Решение победной стратегии:
150 % (28 + 1) = 5
Если первый игрок вытягивает 5 конфет, то на каждом ходу надо будет уравнивать
ход соперника до 29 (28+1). В этом случае первый игрок выиграет точно.
"""

import random

AMOUNT = 150
MAX_TURN = 28


def game():
    player_1 = input("Введите имя игрока: ")
    player_2 = 'PC'
    lucky_flag = False  # счастливый флаг ИИ, если ходит первым, то выиграет
    players = [player_1, player_2]

    first_turn = random.randint(-1, 0)
    # можно и (0,1), но тогда много условий переделывать.
    # Работает - не трогай
    print(f'первым ходит: {players[first_turn + 1]}')

    total = AMOUNT
    while total > 0:
        first_turn += 1
        if players[first_turn % 2] == player_2:
            # ветка ИИ
            print(
                f'\nХодит {players[first_turn % 2]} '
                f'\nНа столе {total}. Берёт: ')

            if total < MAX_TURN + 1:
                step = total
            else:
                if total == AMOUNT:
                    step = AMOUNT % (MAX_TURN + 1)  # чит-код ИИ
                    lucky_flag = True
                else:
                    if lucky_flag:
                        step = MAX_TURN + 1 - step
                        # ИИ берёт: 29 - взятые игроком прошлом ходу
                    else:
                        division = total // MAX_TURN
                        step = total - (division * MAX_TURN + 1)
                        if step == -1:
                            step = MAX_TURN - 1
                        if step == 0:
                            step = MAX_TURN
            print(step)
        else:
            # ветка игрока
            step = int(input(
                f'\nХодит {players[first_turn % 2]} \nНа столе {total} Бери: '))
            while step > MAX_TURN or step > total:
                step = int(input(
                    f'\nЗа один ход можно взять {MAX_TURN} конфет, '
                    f'попробуй еще раз: '))
        total = total - step

    return f'На столе осталось {total} конфет \nПобедил {players[first_turn % 2]}'


if __name__ == "__main__":
    print(game())
