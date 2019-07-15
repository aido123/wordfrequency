"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
import requests
from wordfrequency.exception import WikiException
from wordfrequency.page import Page
import logging

logger = logging.getLogger(__name__)

class WikiPage(Page):
    """
    Class to represent a WIKI Page
    """

    def get_page_text(self):
        """
        Get text from a wiki page using the identifier set on the class
        : return: text str
        """
        logger.info("Get Page Text")
        logger.debug("Page ID: {}".format(self.identifier))
        try:
            response = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json".format(self.identifier))
        except requests.exceptions.RequestException as e:
            logger.error("Exception when reading page: {}".format(str(e)))
            raise WikiException("Exception Reading Page {}".format(str(e)))

        if response.status_code != 200:
            logger.error("API Status Code Error: {}".format(response.status_code))
            raise WikiException("Wikipedia API Error where Status Code = {}".format(str(response.status_code)))
        return response.text
