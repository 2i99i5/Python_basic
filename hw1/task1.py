"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:
6 -> да
7 -> да
1 -> нет
"""


# функция возвращает тип дня, либо ошибку
def weekend_check(number):
    if 6 <= number <= 7:
        return "выходной"
    elif 1 <= number <= 5:
        return "будний"
    else:
        raise Exception('Необходимо ввести число от 1 до 7')


if __name__ == '__main__':
    try:
        num = int(input("Введите число: "))
        print(f'День номер {num}: {weekend_check(num)} день')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
