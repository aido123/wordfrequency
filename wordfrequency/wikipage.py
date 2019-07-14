import requests
from wordfrequency.exception import WikiException
from wordfrequency.page import Page
import logging

logger = logging.getLogger(__name__)

class WikiPage(Page):

    def get_page_text(self):
        logger.info("Get Page Text")
        logger.debug("Page ID: {}".format(self.id))
        try:
            response = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json".format(self.id))
        except requests.exceptions.RequestException as e:
            logger.error("Exception when reading page: {}".format(str(e)))
            raise WikiException("Exception Reading Page {}".format(str(e)))

        if response.status_code != 200:
            logger.error("API Status Code Error: {}".format(response.status_code))
            raise WikiException("Wikipedia API Error where Status Code = {}".format(str(response.status_code)))
        return response.text
