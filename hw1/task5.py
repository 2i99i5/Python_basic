"""
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ:
найти расстояние в 3D пространстве)
Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21
"""
from decimal import Decimal  # для точного округления


def make_coords_from_string(input_str, separ=' '):
    # если нечётное число элементов, то последний элемент не берём
    numbers = list(map(int, input_str.split(separ)))
    len_coord = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return numbers[:len_coord], numbers[len_coord:]
    else:
        return numbers[:len_coord], numbers[len_coord:-1]


def coord_length(coordA, coordB):
    result = sum([(j - k) ** 2 for k, j in zip(coordA, coordB)]) ** 0.5
    # округляем до двух знаков после запятой
    result = Decimal(str(int(result * 100))) / 100
    return result


if __name__ == '__main__':
    try:
        num = input("Введите координаты двух точек через пробел: ")
        # tuple для вывода в круглых скобках
        coordA = tuple(make_coords_from_string(num)[0])
        coordB = tuple(make_coords_from_string(num)[1])
        print(f'Расстояние между точками A {coordA} и B {coordB} '
              f'равно {coord_length(coordA, coordB)}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
