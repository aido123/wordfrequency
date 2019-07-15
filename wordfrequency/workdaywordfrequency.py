"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""

from itertools import islice
from collections import Counter
import re
import logging
from wordfrequency.wordfrequency import WordFrequency

LOGGER = logging.getLogger(__name__)

class WorkdayWordFrequency(WordFrequency):
    """
    Workday Word Frequency Implementation class.
    """

    def count_words(self):
        """
        Count the number of words in a piece of text. A word is defined as a sequence of at least
        four alphabetic characters.
        :return: returns list of (word, count) tuples
        """
        LOGGER.info("Counting Words}")

        #Use the regex \b word boundary with the pattern we want in between.
        four_char_words = re.findall(r"\b[a-zA-Z]{4,}\b", self.text)
        return Counter(four_char_words).items()


    def top_words(self):
        """
        Return the 'n' most common words.
        Words which appear the same number of times (i.e. Jack and Jill appear 19 times) will be
        count as 1 'n' result
        :return: returns list
        """
        LOGGER.info("Counting Top Words")
        LOGGER.debug('Counting Top %s Words', self.n)
        #Add unique word frequencies to a set and sort high -> low and keep top n
        words = self.count_words()
        numbers_frequency = set()
        for word, freq in words:
            numbers_frequency.add(freq)
        numbers_frequency = sorted(numbers_frequency, reverse=True)

        top_numbers_frequency = islice(numbers_frequency, int(self.n))

        #Iterate sorted set and word list and extract word,freq. Words with the same freq
        #will be added to next list. Complexity: O(amount of top words * all words)
        top_words = []
        for number in top_numbers_frequency:
            same_freq = []
            for word, freq in words:
                if number == freq:
                    same_freq.append((word, freq))
            top_words.append(same_freq)
        return top_words
