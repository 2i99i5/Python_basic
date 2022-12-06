"""
B. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.

НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
Расширить значение коэффициентов до [-100..100]
"""
from task01 import *


def read_file(name, flag='r'):
    with open(name, flag) as f:
        return f.read()


def parsing(equation):
    equation = equation.replace(' ', '')  # убираем пробелы
    equation = equation.replace('-', '+-')  # если коэффициенты отрицательные
    equation = equation[:-2].split('+')  # отсекаем "=0"
    if equation[0] == '':  # если первое слагаемое со знаком "-"
        equation.pop(0)
    dict_data = {}
    for item in equation:
        if item.isdigit():
            dict_data[0] = int(item)
        else:
            temp = item.split("*x**")
            if len(temp) > 1:
                dict_data[int(temp[1])] = int(temp[0])
            else:
                temp = item.split("*x")
                dict_data[1] = int(temp[0])
    return dict_data


if __name__ == "__main__":
    path1: str = "taskA.txt"
    data1 = read_file(name=path1)
    path2: str = "taskB.txt"
    data2 = read_file(name=path2)

    dict1 = parsing(data1)
    dict2 = parsing(data2)

    print(f'{dict1}')
    # {8: 20, 7: 30, 6: 68, 4: 71, 3: -60, 2: 62, 1: 17, 0: 73}
    print(f'{dict2}')
    # {5: -33, 4: 100, 3: 95, 2: -81, 1: 13}

    # для правильной длины словаря
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)

    # заполняем словарь суммами элементов
    for key, value in dict3.items():
        dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)
    # {8: 20, 7: 30, 6: 68, 4: 171, 3: 35, 2: -19, 1: 30, 0: 73, 5: -33}

    print(f'{dict3}')

    # запись в файл, когда пофиксю сборку строки с отрицательными элементами
    # str_dict3 = make_str_from_equation(dict3)
    # write_file(data=str_dict3, name='result.txt')
