from itertools import islice
from abc import ABC, abstractmethod

class WordFrequency(ABC):

    def __init__(self, text, n):
        self.text = text
        self.n = n
        super(WordFrequency, self).__init__()

    @abstractmethod
    def count_words(self):
        pass

    @abstractmethod
    def top_words(self):
        pass
