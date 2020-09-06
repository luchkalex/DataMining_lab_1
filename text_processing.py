from re import sub
from stemming.porter2 import stem
from services import get_list_of_lines_from_file
from constants import SOURCE_DIR


# Riding of special characters, multi whitespaces and converting to lower case
def cleanup_text(source):
    result_str = ""

    for line in source:
        result_str += sub("am, ", "am,", sub("(\\s{2,})", " ", sub("([^a-zA-Z\\s,\n])|,,,", " ", line.lower()))) + "\n"

    return result_str


# Deleting stop words from external file
def delete_stop_words(sw_filename, src_string):
    for x in range(2):
        stop_words_file = open(SOURCE_DIR + "/" + sw_filename, "r")

        stop_words_list = get_list_of_lines_from_file(stop_words_file)

        for line in stop_words_list:
            src_string = sub("( " + line + " )|(\n" + line + " )|( " + line + "\n)", " ", src_string)
            src_string = sub("(," + line + " )", ",", src_string)

    return src_string


# Stemming of list of strings
def stem_list(src_list):
    for i in range(len(src_list) - 1):
        src_list[i] = stem(src_list[i])

    return src_list
