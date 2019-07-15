"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from abc import ABC, abstractmethod

class WordFrequencyOutput(ABC):
    """
    Base Workd Frequency Output class.
    """

    def __init__(self, words, n):
        """
        Constructor
        : param: list of number, word tuples list
        : param: n number of words expected str
        """
        self.words = words
        self.n = n
        super(WordFrequencyOutput, self).__init__()

    @abstractmethod
    def format(self):
        """
        Return a Str representation of the output list of top n words
        """
        pass