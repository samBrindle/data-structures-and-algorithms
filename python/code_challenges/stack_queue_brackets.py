from data_structures.queue import Queue
import re


def multi_bracket_validation(string):
    regex = r"[{|(|[|}|)|\]]"
    prev_value = None

    check_list = re.findall(regex, string)

    if check_list[0] == ']' or check_list[0] == '}' or check_list[0] == ')':
        return False
    for char in check_list:
        if prev_value is None:
            if char == '{' or char == '[' or char == '(':
                prev_value = char
        else:
            # check if new opening bracket, if so recursive
            if (char == '{' or char == '[' or char == '(') and\
                    (prev_value == '{' or prev_value == '[' or prev_value == '('):
                new_list = check_list
                new_list.pop(0)
                new_string = ''.join(new_list)
                if not multi_bracket_validation(new_string):
                    return True

            if prev_value == '{':
                if char == ']' or char == ')':
                    return False
            if prev_value == '[':
                if char == '}' or char == ')':
                    return False
            if prev_value == '(':
                if char == ']' or char == '}':
                    return False

            prev_value = char

            if char == '}' or char == ']' or char == ')':
                prev_value = None
    return True


