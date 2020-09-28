from services import get_word_count_list_from_file, get_list_of_lines_from_file
from constants import *
from text_processing import stem_list, cleanup_string

# Naive Bayes classifier


def get_probability_of_ham():
    ham_mes_quantity = len(get_list_of_lines_from_file(HAM_MESSAGES_OUTPUT_FILENAME))
    spam_mes_quantity = len(get_list_of_lines_from_file(SPAM_MESSAGES_OUTPUT_FILENAME))
    return ham_mes_quantity/(ham_mes_quantity + spam_mes_quantity)


def get_probability_of_word(source_word, source_list, quantity_of_words):
    for word in source_list:
        if word.word == source_word:
            return int(word.count)/quantity_of_words

    for word in source_list:
        word.count = str(int(word.count) + 1)

    return 1/quantity_of_words


def calc_quantity_of_words(source_list):
    result = 0
    for word_count in source_list:
        result += int(word_count.count)

    return result


def categorize_string(string):
    ham_result = P_HAM
    spam_result = P_SPAM
    string = cleanup_string(string)
    words_list = string.split()
    words_list = stem_list(words_list)

    ham_list = get_word_count_list_from_file(HAM_WORDS_STAT_OUTPUT_FILENAME)
    spam_list = get_word_count_list_from_file(SPAM_WORDS_STAT_OUTPUT_FILENAME)

    quantity_ham_words = calc_quantity_of_words(ham_list)
    quantity_spam_words = calc_quantity_of_words(spam_list)

    for word in words_list:
        ham_result *= get_probability_of_word(word, ham_list, quantity_ham_words)

    for word in words_list:
        spam_result *= get_probability_of_word(word, spam_list, quantity_spam_words)

    result = ham_result/(ham_result + spam_result)
    if result > 0.5:
        print("It is ham")
    else:
        print("It is spam")


P_HAM = get_probability_of_ham()
P_SPAM = 1 - P_HAM

while 1:
    user_input_string = input("Enter your string")
    categorize_string(user_input_string)

