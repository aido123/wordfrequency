from wordfrequency.wikipage import get_page_text
from wordfrequency.exception import WikiException
from unittest import TestCase
from requests.models import Response
from unittest.mock import patch, mock_open
import mock

class TestWikiPage(TestCase):

    def mocked_requests_get_200(*args, **kwargs):
        the_response = Response()
        the_response.status_code = 200
        the_response._content = b'{"text": "this contains loads of text"}'
        return the_response

    @mock.patch('requests.get', side_effect=mocked_requests_get_200)
    def test_get_page(self, mockget):
        expected = '{"text": "this contains loads of text"}'
        output = get_page_text(88)
        self.assertEqual(output, expected)

    def mocked_requests_get_401(*args, **kwargs):
        the_response = Response()
        the_response.status_code = 401

        return the_response

    @mock.patch('requests.get', side_effect=mocked_requests_get_401)
    def test_get_page_exception_401(self, mockget):

        try:
            output = get_page_text(401401)
            assert False
        except WikiException:
            assert True
