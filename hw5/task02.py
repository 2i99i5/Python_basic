"""
Создайте программу для игры в ""Крестики-нолики""
"""


def print_board(board):
    print('-' * 13)
    for i in range(3):
        print(f'| {board[0 + i * 3]} '
              f'| {board[1 + i * 3]} '
              f'| {board[2 + i * 3]} '
              f'|')
        print('-' * 13)


def choice(tic_tac_toe):
    valid = False
    while not valid:
        player_index = int(input(f'Ход {tic_tac_toe}, выберите ячейку: '))
        if 1 <= player_index <= 9:
            # проверка на то, что клетка занята
            if str(board[player_index - 1]) not in 'X0':
                board[player_index - 1] = tic_tac_toe
                valid = True
            else:
                print('Ячейка занята')
        else:
            print('Нужно ввести цифру от 1 до 9')


def victory_check(board):
    # условия выигрыша
    victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def game(board):
    step = 0
    victory = False
    print_board(board)
    while not victory:
        if step % 2 == 0:
            choice('X')
        else:
            choice('0')
        step += 1
        print_board(board)
        if step >= 5:
            win_check = victory_check(board)
            if win_check:
                return f'Победили {win_check}'
            if step == 9:
                return f'Ничья'


if __name__ == "__main__":
    print('Игра крестики-нолики\n')
    board = list(range(1, 10))
    print(f'{game(board)}')
