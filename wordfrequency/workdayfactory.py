from wordfrequency.abstractfactory import AbstractFactory
from wordfrequency.wikipage import WikiPage
from wordfrequency.workdaywordfrequency import WorkdayWordFrequency
from wordfrequency.workdaywordfrequencyoutput import WorkdayWordFrequencyOutput
import logging

logger = logging.getLogger(__name__)

class WorkdayFactory(AbstractFactory):

    def create_page(self, id):
        return WikiPage(id)

    def create_word_frequency(self, text, n):
        return WorkdayWordFrequency(text, n)

    def create_word_frequency_output(self, words, n):
        return WorkdayWordFrequencyOutput(words, n)