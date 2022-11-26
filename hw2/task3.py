"""
Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE
не использовать! Реализовать свой метод
"""
import random


def shuffle_list(num_list):
    res_list = []
    if not num_list == []:
        while num_list != []:
            i = random.choice(num_list)
            num_list.remove(i)
            res_list.append(i)
    return res_list


if __name__ == '__main__':
    try:
        count = int(input('Введите длину списка: '))
        num_list = list(range(count))
        print(f'Начальный список:    {num_list}')
        result_list = shuffle_list(num_list)
        print(f'Перемешанный список: {result_list}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
