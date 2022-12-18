import model
import view
import logger
from parser_formula import parse
import expression as ex


def input_first():  # первым может быть число или выражение
    enter = view.input_expression()
    if type(enter) == float:
        model.set_first(enter)
    else:
        model.set_formula(enter)


def input_second():  # вторым и последующими может быть только число
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_div_by_zero()
        else:
            model.set_second(number)
            break


def input_operation():
    operation = view.input_operation()
    model.set_operation(operation)


def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()
    result_string = f'{model.get_first()} {model.get_operation()} ' \
                    f'{model.get_second()} = {model.get_result()}'
    logger.calc_logger(result_string)
    view.print_to_console(result_string)
    model.set_first(model.get_result())


def calculation_of_expression():
    # создаётся генератор из распарсеной строки
    generator_formula = parse(model.get_formula())
    # операции сортируются по порядку выполнения
    sorted_generator = ex.shunting_yard(generator_formula)

    try:
        # выполнение операций
        model.set_expression_result(ex.calc(sorted_generator))
    except:
        view.print_div_by_zero()
    # записываем результат в первое число, для последующих операций
    model.set_first(model.get_result())
    result_string = f'{model.get_formula()} = {model.get_result()}'
    logger.calc_logger(result_string)
    view.print_to_console(result_string)


def start():
    input_first()
    if model.get_formula() != '':
        calculation_of_expression()
    while True:
        input_operation()
        if model.get_operation() == '=':
            view.log_off()
            break
        input_second()
        solution()
