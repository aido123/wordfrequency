"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from abc import ABC, abstractmethod

class Page(ABC):
    """
    Base Page class
    """

    def __init__(self, identifier):
        """
        Constructor
        : param: identifier of page: str
        """
        self.identifier = identifier
        super(Page, self).__init__()

    @abstractmethod
    def get_page_text(self):
        """
        Sub Classes to implement this method to return a page of text given an identifier.
        : return: text str
        """
        pass
