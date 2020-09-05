from services import *
from constants import *

src_file = open(SOURCE_DIR + "/" + MAIN_SOURCE_FILENAME, "r")

# Riding of special characters, multi whitespaces and converting to lower case
edited_str = cleanup_text(src_file)

# Converting source string to list of messages
message_list = get_list_of_lines_from_string(edited_str)

# Distribution of messages into categories: ham and spam, and write it to files
categorize_messages_to_file(message_list, HAM_MESSAGES_OUTPUT_FILENAME, SPAM_MESSAGES_OUTPUT_FILENAME)

# Deleting stop words from external file
edited_str = delete_stop_words(STOP_WORDS_SOURCE_FILENAME, edited_str)

# Converting updated string to list of messages
message_list = get_list_of_lines_from_string(edited_str)

# Distribution of words into categories: ham and spam, and write it to files
categorize_words_of_messages_to_file(message_list, HAM_WORDS_STAT_OUTPUT_FILENAME, SPAM_WORDS_STAT_OUTPUT_FILENAME)
