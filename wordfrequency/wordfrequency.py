"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from itertools import islice
from abc import ABC, abstractmethod

class WordFrequency(ABC):
    """
    Base Word Frequency Class.
    """

    def __init__(self, text, n):
        """
        Constructor
        : param: text str
        : param: n top number of words
        """
        self.text = text
        self.n = n
        super(WordFrequency, self).__init__()

    @abstractmethod
    def count_words(self):
        """
        Count the words in a str.
        : return: list of number, word tuple
        """
        pass

    @abstractmethod
    def top_words(self):
        """
        Return the top n words in a list
        : return: list of top n number, word tuple
        """
        pass
