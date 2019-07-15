"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """
    Abstract Factory class which other concrete factories will extend.
    """

    @abstractmethod
    def create_page(self, identifier):
        """
        Abstract method for Creating a Page Object.
        : param: page identifier str
        : return: Page Object
        """
        pass

    @abstractmethod
    def create_word_frequency(self, text, n):
        """
        Abstract method to return a Word Frequency Object.
        : param: text to count words str
        : param: n top words
        : return: WordFrequency Object
        """
        pass

    @abstractmethod
    def create_word_frequency_output(self, words, n):
        """
        Abstract method to return a Word Frequency Output Object.
        : param: words list of tuples
        : param: n total  str
        : return: WordFrequencyOutput Object
        """
        pass
