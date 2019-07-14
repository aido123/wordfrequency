from abc import ABC, abstractmethod

class WordFrequencyOutput(ABC):

    def __init__(self, words, n):
        self.words = words
        self.n = n
        super(WordFrequencyOutput, self).__init__()

    @abstractmethod
    def format(self):
        pass