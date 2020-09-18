from word_stat import *

# Build plot of ham messages length distribution
build_plot_distribution_of_lengths(
    HAM_MESSAGES_OUTPUT_FILENAME, HAM_MESSAGES_LENGTH_PLOT_FILENAME)

# Build plot of spam messages length distribution
build_plot_distribution_of_lengths(
    SPAM_MESSAGES_OUTPUT_FILENAME, SPAM_MESSAGES_LENGTH_PLOT_FILENAME)

# Build plot of ham words length distribution
build_plot_distribution_of_lengths(
    HAM_WORDS_OUTPUT_FILENAME, HAM_WORDS_LENGTH_PLOT_FILENAME)

# Build plot of spam words length distribution
build_plot_distribution_of_lengths(
    SPAM_WORDS_OUTPUT_FILENAME, SPAM_WORDS_LENGTH_PLOT_FILENAME)

# Build plot of ham most frequent words
build_plot_most_frequent_words(
    HAM_WORDS_STAT_OUTPUT_FILENAME, MOST_FREQUENT_HAM_WORDS_PLOT_FILENAME)

# Build plot of spam most frequent words
build_plot_most_frequent_words(
    SPAM_WORDS_STAT_OUTPUT_FILENAME, MOST_FREQUENT_SPAM_WORDS_PLOT_FILENAME)
