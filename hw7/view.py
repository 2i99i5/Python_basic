import re


def input_expression():
    while True:
        enter = input('Введите число или выражение: ')

        # проверяем регулярными выражениями
        # формула
        if re.search(
                "^\(*-?\d+(\.?\d+)?\)?([+\-*\/]{1}\(*-?\d+(\.?\d+)?\)*)+$",
                enter
        ):
            return enter
        # число
        elif re.search(
                "^-?\d+(\.?\d+)?$",
                enter
        ):
            return float(enter)
        else:
            print('Ошибка')


def input_number() -> float:
# для второго и последующих
    while True:
        try:
            number = float(input('Введите число: '))
            return number
        except:
            print('Ошибка')


def input_operation():
    while True:
        operation = input("Введите операцию или '=' для выхода: ")
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию ')


def print_to_console(data):
    print(data)


def log_off():
    print('До свидания! ')


def print_div_by_zero():
    print('На ноль делить нельзя ')
