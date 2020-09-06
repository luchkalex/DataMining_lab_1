from re import *


def get_list_of_lines_from_file(src_file):
    result_list = []

    for line in src_file:
        result_list.append(sub("\n", "", line))

    return result_list


def get_list_of_lines_from_string(src_string):
    return src_string.split("\n")
