"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""


def coord_by_quarter(number):
    switch_case_quarter = {
        1: 'x > 0 and y > 0',
        2: 'x < 0 and y > 0',
        3: 'x < 0 and y < 0',
        4: 'x > 0 and y < 0'
    }
    if number in switch_case_quarter:
        return switch_case_quarter[number]
    else:  # обработка отсутствия значения в словаре
        raise Exception('Необходимо ввести целое число от 1 до 4')


if __name__ == '__main__':
    try:
        num = int(input("Введите номер четверти: "))
        print(f'Для данной четверти: {coord_by_quarter(num)}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
