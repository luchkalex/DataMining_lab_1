import matplotlib.pyplot as plt

from re import *
from constants import *
from models.WordCount import WordCount
from services import get_list_of_lines_from_file, get_quantity_length_list_from_string_list, \
    get_word_count_list_from_file
from text_processing import stem_list


def get_stat_count_of_words(src_list):
    already_in_list = False
    word_count_list = []

    for item in src_list:
        for word_count in word_count_list:
            # If content of found word didn't match any previous
            # -> Add to list this item with it's count
            if item == word_count.word:
                already_in_list = True
        if not already_in_list:
            word_count_list.append(WordCount(item, src_list.count(item)))
            already_in_list = False
        else:
            already_in_list = False

    return word_count_list


# Distribution of messages into categories: ham and spam, and write it to files
def categorize_messages_to_file(msg_list, ham_filename, spam_filename):
    # Lists to distribute in
    ham_list = []
    spam_list = []

    ham_msg_file = open(OUTPUT_DIR + "/" + ham_filename, "w")
    spam_msg_file = open(OUTPUT_DIR + "/" + spam_filename, "w")

    # Distribution into two lists
    for line in msg_list:
        if line.startswith("ham,"):
            ham_list.append(sub("ham,|", "", line))
        elif line.startswith("spam,"):
            spam_list.append(sub("spam,|", "", line))

    # Writing to file
    for item in ham_list:
        ham_msg_file.write(item + "\n")

    for item in spam_list:
        spam_msg_file.write(item + "\n")


# Distribution of words into categories: ham and spam, and write it to files
def categorize_words_of_messages_to_file(msg_list, ham_filename, spam_filename):
    # Lists to distribute in
    ham_list = []
    spam_list = []

    # Distribution into two lists
    for line in msg_list:
        if line.startswith("ham,"):
            ham_list += sub("ham,|,", "", line).split()
        elif line.startswith("spam,"):
            spam_list += sub("spam,|,", "", line).split()

    # Stemming of words in lists
    ham_list = stem_list(ham_list)
    spam_list = stem_list(spam_list)

    # Getting stat of words count
    ham_stat = get_stat_count_of_words(ham_list)
    spam_stat = get_stat_count_of_words(spam_list)

    # Writing into files of stat
    ham_stat_file = open(OUTPUT_DIR + "/" + ham_filename, "w")

    for item in ham_stat:
        ham_stat_file.write(item.word + ": " + str(item.count) + "\n")

    spam_stat_file = open(OUTPUT_DIR + "/" + spam_filename, "w")

    for item in spam_stat:
        spam_stat_file.write(item.word + ": " + str(item.count) + "\n")

    # Writing into files raw words list separated with \n
    ham_file = open(OUTPUT_DIR + "/" + HAM_WORDS_OUTPUT_FILENAME, "w")

    for item in ham_stat:
        ham_file.write(item.word + "\n")

    spam_file = open(OUTPUT_DIR + "/" + SPAM_WORDS_OUTPUT_FILENAME, "w")

    for item in spam_stat:
        spam_file.write(item.word + "\n")


# Build plot of length of lines from file.
# It needed work with words, words have to be separated with \n
def build_plot_distribution_of_lengths(src_filename, output_filename):
    src_file = open(OUTPUT_DIR + "/" + src_filename, "r")
    # List of lines to work with
    src_list = get_list_of_lines_from_file(src_file)

    quantity_lengths_list = []
    lengths_list = []
    quantities_list = []

    # To find out average length of strings
    average_length = 0

    quantity_lengths_list = get_quantity_length_list_from_string_list(src_list)

    # Sorting by length
    quantity_lengths_list.sort(key=lambda x: int(x.length), reverse=False)

    # Splitting the list in two (lengths and quantities) to build plot
    for item in quantity_lengths_list:
        lengths_list.append(item.length)
        quantities_list.append(item.quantity / len(src_list))

    # Calc average length
    for i in range(0, len(lengths_list)):
        average_length += lengths_list[i] * quantities_list[i]

    average_length = round(average_length/sum(quantities_list))

    # Build plot
    plt.plot(lengths_list, quantities_list)
    plt.grid()
    plt.title("Length distribution")
    plt.xlabel("Length\nAverage length: " + str(average_length))
    plt.ylabel("Quantity")
    plt.savefig(OUTPUT_DIR + "/" + output_filename)
    plt.show()


# Build plot of 20 most frequent words from file
# It works with a file format like "word: count". For example "the: 9"
def build_plot_most_frequent_words(src_filename, plot_filename):
    src_file = open(OUTPUT_DIR + "/" + src_filename, "r")

    # Lists for plot building
    most_frequent_words = []
    most_frequent_words_counts = []

    word_count_list = get_word_count_list_from_file(src_file)

    # Sorting by count of words
    word_count_list.sort(key=lambda word: int(word.count), reverse=True)

    # Take first 20 words and distribute into two lists to build plot
    for x in range(20):
        most_frequent_words.append(word_count_list[x].word)
        most_frequent_words_counts.append(int(word_count_list[x].count))

    # Build plot
    fig, ax = plt.subplots()
    ax.bar(most_frequent_words, most_frequent_words_counts)
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    plt.xticks(rotation='vertical')
    plt.title("Most frequent words")
    plt.xlabel("Word")
    plt.ylabel("Quantity")
    plt.savefig(OUTPUT_DIR + "/" + plot_filename)
    plt.show()
