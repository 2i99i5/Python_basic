"""
Задайте список из n чисел последовательности (1 + 1/n)^n.
Вывести в консоль сам список и сумму его элементов.
"""


def make_list(num):
    res_list = []
    for i in range(num):
        res_list.append(round((1 + 1 / (i + 1) ** (i + 1)), 4))
    return res_list


if __name__ == '__main__':
    try:
        count = int(input('Введите число: '))
        result_list = make_list(count)
        print(f'Список: {result_list}')
        print(f'Сумма элементов: {sum(result_list)}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
