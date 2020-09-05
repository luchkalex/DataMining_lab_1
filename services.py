from re import *
from stemming.porter2 import stem
import matplotlib.pyplot as plt
from models.StringLength import StringLength
from constants import *
from models.WordCount import WordCount


def stem_list(src_list):
    for i in range(len(src_list) - 1):
        src_list[i] = stem(src_list[i])
    return src_list


def get_list_of_lines_from_file(src_file):
    result_list = []

    for line in src_file:
        result_list.append(sub("\n", "", line))

    return result_list


def get_list_of_lines_from_string(src_string):
    return src_string.split("\n")


def build_plot_distribution_of_length(src_filename, output_filename):
    src_file = open(OUTPUT_DIR + "/" + src_filename, "r")
    src_list = get_list_of_lines_from_file(src_file)

    stat = []
    stat_length = []
    stat_quantity = []
    already_in_list = False
    average_sum = 0

    for line in src_list:
        for src_string in stat:
            if len(line) == src_string.length:
                already_in_list = True
                break
        if not already_in_list:
            stat.append(StringLength(1, len(line)))
            already_in_list = False
        else:
            stat[stat.index(src_string)].quantity += 1
            already_in_list = False

    stat.sort(key=lambda x: int(x.length), reverse=False)

    for line in stat:
        stat_length.append(line.length)
        stat_quantity.append(line.quantity)

    for line in stat:
        print(str(line.length) + ": " + str(line.quantity))

    for i in range(0, len(stat_length)):
        average_sum += stat_length[i] * stat_quantity[i]

    average_sum = round(average_sum/sum(stat_quantity))

    plt.plot(stat_length, stat_quantity)
    plt.grid()
    plt.title("Length distribution")
    plt.xlabel("Length\nAverage length: " + str(average_sum))
    plt.ylabel("Quantity")
    plt.savefig(OUTPUT_DIR + "/" + output_filename)
    plt.show()


def cleanup_text(source):
    result_str = ""

    # To lower case
    for line in source:
        result_str += sub("am, ", "am,", sub("(\\s{2,})", " ", sub("([^a-zA-Z\\s,\n])|,,,", " ", line.lower()))) + "\n"

    return result_str


def delete_stop_words(sw_filename, src_string):
    for x in range(2):
        # Deleting stop words from source_files
        stop_words_file = open(SOURCE_DIR + "/" + sw_filename, "r")

        # Fill list of words
        stop_words_list = get_list_of_lines_from_file(stop_words_file)

        # Delete from source_files
        for line in stop_words_list:
            src_string = sub("( " + line + " )|(\n" + line + " )|( " + line + "\n)", " ", src_string)
            src_string = sub("(," + line + " )", ",", src_string)

    return src_string


def categorize_messages_to_file(msg_list, ham_filename, spam_filename):
    ham_list = []
    spam_list = []
    ham_msg_file = open(OUTPUT_DIR + "/" + ham_filename, "w")
    spam_msg_file = open(OUTPUT_DIR + "/" + spam_filename, "w")

    for line in msg_list:
        if line.startswith("ham,"):
            ham_list.append(sub("ham,|", "", line))
        elif line.startswith("spam,"):
            spam_list.append(sub("spam,|", "", line))

    for item in ham_list:
        ham_msg_file.write(item + "\n")

    for item in spam_list:
        spam_msg_file.write(item + "\n")


def get_stat_count_of_words(src_list):
    already_in_list = False
    word_stat = []
    for item in src_list:
        for word_count in word_stat:
            if item == word_count.word:
                already_in_list = True
        if not already_in_list:
            word_stat.append(WordCount(item, src_list.count(item)))
            already_in_list = False
        else:
            already_in_list = False
    return word_stat


def categorize_words_of_messages_to_file(msg_list, ham_filename, spam_filename):
    ham_list = []
    spam_list = []

    for line in msg_list:
        if line.startswith("ham,"):
            ham_list += sub("ham,|,", "", line).split()
        elif line.startswith("spam,"):
            spam_list += sub("spam,|,", "", line).split()

    ham_list = stem_list(ham_list)
    spam_list = stem_list(spam_list)

    ham_stat = get_stat_count_of_words(ham_list)
    spam_stat = get_stat_count_of_words(spam_list)

    ham_stat_file = open(OUTPUT_DIR + "/" + ham_filename, "w")

    for item in ham_stat:
        ham_stat_file.write(item.word + ": " + str(item.count) + "\n")

    spam_stat_file = open(OUTPUT_DIR + "/" + spam_filename, "w")

    for item in spam_stat:
        spam_stat_file.write(item.word + ": " + str(item.count) + "\n")

    ham_file = open(OUTPUT_DIR + "/" + HAM_WORDS_OUTPUT_FILENAME, "w")

    for item in ham_stat:
        ham_file.write(item.word + "\n")

    spam_file = open(OUTPUT_DIR + "/" + SPAM_WORDS_OUTPUT_FILENAME, "w")

    for item in spam_stat:
        spam_file.write(item.word + "\n")


def build_plot_most_frequent_words(src_filename, plot_filename):
    # put into list of WordCount objects from words file
    # sort list by word frequency
    # take first 20 words
    # put into lists of length and frequency
    # build plot
    src_file = open(OUTPUT_DIR + "/" + src_filename, "r")
    word_count_list = []
    most_frequent_words_lengths = []
    most_frequent_words_counts = []

    for line in src_file:
        word_count_list.append(WordCount(sub(":.*\n", "", line), sub("\\D*", "", line)))

    word_count_list.sort(key=lambda x: int(x.count), reverse=True)

    for x in range(20):
        most_frequent_words_lengths.append(word_count_list[x].word)
        most_frequent_words_counts.append(word_count_list[x].count)

    plt.plot(most_frequent_words_lengths, most_frequent_words_counts, "bo-")
    plt.grid()
    plt.xticks(rotation='vertical')
    plt.title("Most frequent words")
    plt.xlabel("Word")
    plt.ylabel("Quantity")
    plt.savefig(OUTPUT_DIR + "/" + plot_filename)
    plt.show()
