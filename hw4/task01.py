"""
A. Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать
в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть =>
2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
Расширить значение коэффициентов до [-100..100]
"""
import random


def make_str_from_equation(dict_equation: dict):
    equation = ''
    for i in range(len(dict_equation) - 1, -1, -1):
        if dict_equation[i] != 0:
            if dict_equation[i] == 1:
                if i == 1:
                    equation += 'x + '
                elif i == 0:
                    equation += '1 '
                else:
                    equation += f'x**{i} + '
            else:
                if i == 1:
                    equation += f'{dict_equation[i]}*x + '
                elif i == 0:
                    equation += f'{dict_equation[i]} '
                else:
                    equation += f'{dict_equation[i]}*x**{i} + '
    equation = equation.replace('+ -', '- ')  # обработка отрицательных
    return equation + '= 0'


def make_equation(size: int):
    koef = {}
    for i in range(size + 1):
        koef[i] = random.randint(-100, 101)
    str_equation = make_str_from_equation(koef)
    # print(koef)

    return str_equation


def write_file(name: str, data: str, flag='w'):
    with open(name, flag) as f:
        f.write(data)


if __name__ == "__main__":
    k1 = int(input('Введите максимальную степень первого многочлена: '))
    data1 = make_equation(k1)
    print(data1)
    write_file(data=data1, name='taskA.txt')

    k2 = int(input('Введите максимальную степень второго многочлена: '))
    data2 = make_equation(k2)
    print(data2)
    write_file(data=data2, name='taskB.txt')

    # neg_dict = {0: -1, 1: 65, 2: -24, 3: -57, 4: 89, 5: -96}
    # neg_equation = make_str_from_equation(neg_dict)
    # print(neg_equation)
