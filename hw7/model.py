first_number = 0
second_number = 0
operator = ''
result = 0
formula_string = ''


def get_formula():
    global formula_string
    return formula_string


def get_first():
    global first_number
    return first_number


def get_second():
    global second_number
    return second_number


def get_operation():
    global operator
    return operator


def get_result():
    global result
    return result


def set_formula(value):
    global formula_string
    formula_string = value


def set_first(value):
    global first_number
    first_number = value


def set_second(value):
    global second_number
    second_number = value


def set_operation(oper):
    global operator
    operator = oper


def addition():
    global first_number
    global second_number
    global result
    result = first_number + second_number


def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number


def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number


def division():
    global first_number
    global second_number
    global result
    result = first_number / second_number


def set_expression_result(value):
    global result
    result = value
