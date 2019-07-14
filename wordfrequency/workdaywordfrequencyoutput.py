from wordfrequency.exception import WikiException
from wordfrequency.wordfrequencyoutput import WordFrequencyOutput
import logging

logger = logging.getLogger(__name__)

class WorkdayWordFrequencyOutput(WordFrequencyOutput):

    def format(self):
        """
        Formats a nested list of (word, count) tuples into a human readable output.
        Where a nested list occurs, the words in that list will be dispalyed on the same line
        :return: returns string output
        """
        logger.info("Formatting Top Words")
        output = "Top {} words:\n".format(self.n)

        for nested_list in self.words:
            same_freq_words = []
            for word,freq in nested_list:
                same_freq_words.append(word)
            output += "- {} {} \n".format(freq, ', '.join(same_freq_words))
        return output
