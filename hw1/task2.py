"""
Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
# импорт reduce
from functools import reduce
# красивые таблицы, необходимо выполнить в терминале: pip install tabulate
from tabulate import tabulate


CONST = 3  # количество предикат
table = []
for i in range(2 ** CONST):
    # преобразуем число от 0 до 2**CONST в список бит
    list_i = [1 if i & (1 << (CONST - 1 - n)) else 0 for n in range(CONST)]
    # список бит для вычисления второй функции
    invert = [0 if i & (1 << (CONST - 1 - n)) else 1 for n in range(CONST)]
    # функция ¬(X ⋁ Y ⋁ Z)
    func1 = int(not reduce(lambda x, y: x or y, list_i))
    # функция ¬X ⋀ ¬Y ⋀ ¬Z
    func2 = reduce(lambda x, y: x and y, invert)
    # добавляем столбцы с функциями
    list_i.append(func1)
    list_i.append(func2)
    # дописываем в таблицу "строку"
    table.append(list_i)
# вывод таблицы table
print(tabulate(
    table,
    headers=['X', 'Y', 'Z', '¬(X ⋁ Y ⋁ Z)', '¬X ⋀ ¬Y ⋀ ¬Z'],
    tablefmt='fancy_grid'
)
)
