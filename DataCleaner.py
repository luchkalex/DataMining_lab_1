from services import *
from constants import *

src_file = open(SOURCE_DIR + "/" + MAIN_SOURCE_FILENAME, "r")

edited_str = cleanup_text(src_file)

message_list = get_list_of_lines_from_string(edited_str)

categorize_messages_to_file(message_list, HAM_MESSAGES_OUTPUT_FILENAME, SPAM_MESSAGES_OUTPUT_FILENAME)

edited_str = delete_stop_words(STOP_WORDS_SOURCE_FILENAME, edited_str)

message_list = get_list_of_lines_from_string(edited_str)

categorize_words_of_messages_to_file(message_list, HAM_WORDS_STAT_OUTPUT_FILENAME, SPAM_WORDS_STAT_OUTPUT_FILENAME)
