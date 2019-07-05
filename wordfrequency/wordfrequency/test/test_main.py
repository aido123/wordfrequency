
from wordfrequency.main import parse_args, main
from wordfrequency.exception import WikiException

from unittest import TestCase
from requests.models import Response
from unittest.mock import patch, mock_open
import mock
import sys

class TestMain(TestCase):

    def test_parse_args_success_default_value(self):
        basic_args = ['--page_id', '4']

        parser = parse_args(basic_args)
        assert (parser.n == 5)
        assert (parser.page_id == '4')

    def test_parse_args_missing_arg(self):
        basic_args = ['--n', '3']

        with self.assertRaises(SystemExit) as err:
            parser = parse_args(basic_args)
        self.assertRaises(SystemExit)

    def test_main_happy(self):
        with patch('sys.argv', ['None', '--page_id', '21721040', '--n', '5']):
            try:
                main()
                assert(True)
            except:
                assert(False)
