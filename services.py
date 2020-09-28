from re import *

from models.QuantityLength import QuantityLength
from models.WordCount import WordCount


def get_list_of_lines_from_file(src_file):
    result_list = []

    for line in src_file:
        result_list.append(sub("\n", "", line))

    return result_list


def get_list_of_lines_from_string(src_string):
    return src_string.split("\n")


def get_quantity_length_list_from_string_list(src_list):
    quantity_lengths_list = []

    # Flag that show if strings length was already found
    already_in_list = False

    for item in src_list:
        for quantity_length in quantity_lengths_list:
            # If length of found string match any previous
            # -> inc quantity of this item
            if len(item) == quantity_length.length:
                already_in_list = True
                break
        if not already_in_list:
            quantity_lengths_list.append(QuantityLength(1, len(item)))
            already_in_list = False
        else:
            # Find item of matched strings and inc
            quantity_lengths_list[quantity_lengths_list.index(quantity_length)] \
                .quantity += 1
            already_in_list = False

    return quantity_lengths_list


def get_word_count_list_from_file(src_file):
    word_count_list = []
    # Parse file into list of WordCount
    for line in src_file:
        word_count_list.append(WordCount(sub(":.*\n", "", line), sub("\\D*", "", line)))
    return word_count_list
