import re


def get_validation_regex():
    white_list = '''acos|asin|atan|atan2|ceil|cos|cosh|
        degrees|exp|fabs|floor|fmod|frexp|hypot|ldexp|
        log|log10|modf|pow|radians|sin|sinh|sqrt|tan|tanh'''
    regex_string = '[^' + white_list + '|0-9|+\-\*/\^\(\).//]'
    return re.compile(regex_string)


def is_valid_input(func_string):
    regex = get_validation_regex()
    match = regex.search(func_string)
    if match == None:
        return True
    else:
        return False


def calculate(func_string):
    if is_valid_input(func_string):
        func_string = func_string.replace("^", "**")
        try:
            answer = str(eval(func_string))
            return answer
        except:
            return "error"
    else:
        return "error"


def calculate_list(func_list):
    new_list = []
    for i in range(len(func_list)):
        func_string = func_list[i]
        new_list.append((func_string, calculate(func_string)))
    return new_list