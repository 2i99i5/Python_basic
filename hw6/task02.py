"""
ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
Написать программу, которая состоит 4 из этапов:
- создает список из рандомных четырехзначных чисел
- принимает с консоли цифру и удаляет ее из всех элементов списка
- цифры каждого элемента суммирует пока результат не станет однозначным числом
- из финального списка убирает все дублирующиеся элементы
- после каждого этапа выводить результат в консоль
Пример:
- 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
- 2 этап: Введите цифру: 3
- 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
- 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
- 3 этап: [3, 1, 5, 5, 3, 5, 4]
- 4 этап: [3, 1, 5, 4]
"""
import random

# 1 этап:
count = int(input('Введите длину списка: '))
# List Comprehension
_list = [random.randint(0, 10000) for i in range(count)]
print(_list)
# 2 этап:
del_digit = input('Введите цифру, которую надо удалить: ')
temp_list = []
for i in _list:
    i = str(i)
    temp = ''
    for j in i:
        if j != del_digit:
            temp += j
    temp_list.append(int(temp))
print(temp_list)


# 3 этап:
def sum_digits(num):
    # рекурсивная функция сложения цифр в числе
    if num > 9:
        return num % 10 + sum_digits(num // 10)
    else:
        return num


_list = []
for i in temp_list:
    while i > 9:  # если в результате число больше одной цифры
        i = sum_digits(i)
    _list.append(i)
print(_list)

# 4 этап:

# temp_list = []
# for i in _list:
#     if i not in temp_list:
#         temp_list.append(i)

# List Comprehension
temp_list = [i for i in _list if i not in temp_list]

_list = temp_list

print(_list)
