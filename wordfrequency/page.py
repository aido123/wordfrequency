from abc import ABC, abstractmethod

class Page(ABC):

    def __init__(self, id):
        self.id = id
        super(Page, self).__init__()

    @abstractmethod
    def get_page_text(self):
        pass
