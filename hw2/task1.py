"""
Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
"""


def sum_of_digit(number):
    num_str = str(number)
    digit_sum = 0
    for i in num_str:
        if i.isdigit():
            digit_sum += int(i)
    return digit_sum


if __name__ == '__main__':
    try:
        num = float(input('Введите вещественное число: '))
        print(f'Сумма цифр числа: {sum_of_digit(num)}')
    except (ValueError, Exception) as err:
        print('Ошибка!', err)
