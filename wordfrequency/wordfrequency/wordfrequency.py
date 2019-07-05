from itertools import islice
from collections import Counter
import re
import logging

logger = logging.getLogger(__name__)

def count_words(text):
    """
    Count the number of words in a piece of text. A word is defined as a sequence of at least four alphabetic characters.
    :param text: str pasage of text
    :return: returns list of (word, count) tuples
    """
    logger.info("Counting Words}")
    four_char_words = re.findall(r"\b[a-zA-Z]{4,}\b",text)
    return Counter(four_char_words).items()


def top_words(words, n):
    """
    Return the 'n' most common words.
    Words which appear the same number of times (i.e. Jack and Jill appear 19 times) will be count as 1 'n' result
    :param words: list of (word, count) tuples
    :param n: The top number of words
    :return: returns list
    """
    logger.info("Counting Top Words")
    logger.debug("Counting Top {} Words".format(n))
    #Add unique word frequencies to a set and sort high -> low and keep top n
    numbers_frequency = set()
    for word, freq in words:
       numbers_frequency.add(freq)
    numbers_frequency = sorted(numbers_frequency, reverse=True)

    top_numbers_frequency = islice(numbers_frequency, n)

    #Iterate sorted set and word list and extract word,freq. Words with the same freq will be added to next list
    top_words = []
    for number in top_numbers_frequency:
        same_freq = []
        for word, freq in words:
            if number == freq:
                same_freq.append((word,freq))
        top_words.append(same_freq)
    return top_words

def format(words, n):
    """
    Formats a nested list of (word, count) tuples into a human readable output.
    Where a nested list occurs, the words in that list will be dispalyed on the same line
    :param words: nested list of (word, count) tuples
    :param n: The top number of words to be presented
    :return: returns list
    """
    logger.info("Formatting Top Words")
    output = "Top {} words:\n".format(n)

    for nested_list in words:
        same_freq_words = []
        for word,freq in nested_list:
            same_freq_words.append(word)
        output += "- {} {} \n".format(freq, ', '.join(same_freq_words))
    return output
