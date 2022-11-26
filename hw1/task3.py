"""
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).
Пример:
x=34; y=-30 -> 4
x=2; y=4 -> 1
x=-34; y=-30 -> 3
"""


def quarter_definition(x, y):
    if x == 0:
        if y == 0:
            raise Exception('Должно выполняться условие: X ≠ 0 и Y ≠ 0')
        else:
            return "на оси x"
    elif x > 0:
        if y == 0:
            return "на оси y"
        elif y > 0:
            return "в первой четверти"
        else:
            return "в четвёртой четверти"
    elif x < 0:
        if y == 0:
            return "на оси y"
        elif y > 0:
            return "во второй четверти"
        else:
            return "в третьей четверти"


if __name__ == '__main__':
    try:
        x = int(input("Введите координату x: "))
        y = int(input("Введите координату y: "))
        print(f'Точка находится {quarter_definition(x, y)}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
