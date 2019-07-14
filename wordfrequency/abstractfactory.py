from abc import ABC, abstractmethod

class AbstractFactory(ABC):

#    def __init__(self, id):
#        self.id = id
#        super(AbstractFactory, self).__init__()

    @abstractmethod
    def create_page(self, id):
        pass

    @abstractmethod
    def create_word_frequency(self, text, n):
        pass

    @abstractmethod
    def create_word_frequency_output(self, words, n):
        pass
