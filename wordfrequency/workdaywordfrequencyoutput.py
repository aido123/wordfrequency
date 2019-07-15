"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
import logging

from wordfrequency.wordfrequencyoutput import WordFrequencyOutput

LOGGER = logging.getLogger(__name__)

class WorkdayWordFrequencyOutput(WordFrequencyOutput):
    """
    Workday Word Frequency Output Implementation Class.
    """

    def format(self):
        """
        Formats a nested list of (word, count) tuples into a human readable output.
        Where a nested list occurs, the words in that list will be dispalyed on the same line
        :return: returns string output
        """
        LOGGER.info("Formatting Top Words")
        output = "Top {} words:\n".format(self.n)

        for nested_list in self.words:
            same_freq_words = []
            frequency_number = ""
            for word, freq in nested_list:
                same_freq_words.append(word)
                frequency_number = freq
            output += "- {} {} \n".format(frequency_number, ', '.join(same_freq_words))
        return output
