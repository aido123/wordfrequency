"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from wordfrequency.abstractfactory import AbstractFactory
from wordfrequency.wikipage import WikiPage
from wordfrequency.workdaywordfrequency import WorkdayWordFrequency
from wordfrequency.workdaywordfrequencyoutput import WorkdayWordFrequencyOutput

class WorkdayFactory(AbstractFactory):
    """
    Concrete Factory for Workday Word Frequency Counter.
    """

    def create_page(self, identifier):
        """
        Create a Wiki Page Object
        : param: wiki page identifier
        : return: WikiPage object
        """
        return WikiPage(identifier)

    def create_word_frequency(self, text, n):
        """
        Create a Workday Word Frequency Object
        : param: text of data str
        : param: top n words to count
        : return: WorkdayWordFrequency Object
        """
        return WorkdayWordFrequency(text, n)

    def create_word_frequency_output(self, words, n):
        """
        Create a WorkdayWordFrequencyOutput
        : param: list of number, word tuples
        : param: number of n words expected
        : return: WorkdayWordFrequencyOutput Object
        """
        return WorkdayWordFrequencyOutput(words, n)
