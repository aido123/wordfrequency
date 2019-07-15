"""
Copyright (C) 2019 Adrian Hynes <adrianhynes@gmail.com>
"""
from wordfrequency.page import Page
from wordfrequency.wordfrequencyoutput import WordFrequencyOutput
from wordfrequency.wordfrequency import WordFrequency
from wordfrequency.factoryproducer import FactoryProducer

import argparse
import sys
from termcolor import cprint
from wordfrequency.exception import WikiException
import logging
import logging.config

LOGGER = logging.getLogger(__name__)

WORKDAY_TYPE = "workday"

"""
Entry point module for Top Wiki Pae Word Frequency Counter.
"""

def parse_args(args):
    """
    Parse the command line params, use defaults from properties if needed.
    Args:
        args: List of Arguments.
    Returns:
        str: Parsed Arguments.
    """
    LOGGER.info("Parsing Arguments")
    parser = argparse.ArgumentParser()
    parser.add_argument('--page_id', help='Wiki Page ID', required=True)
    parser.add_argument('--n', help='Top n item to return. Defaults to 5.', required=False)
    parsed_args = parser.parse_args(args)

    if parsed_args.n is None:
        parsed_args.n = 5

    LOGGER.debug("Arguments {}".format(parsed_args))
    return parsed_args

def main():
    """
    Entry Point to Top Wiki Page Word Frequency Counter.
    """
    try:
        #Parse command line args
        args = parse_args(sys.argv[1:])

        #Get our page, wordfrequency and wordfrequencyouts impl's using a factory producer implementation.
        factory = FactoryProducer().get_factory(WORKDAY_TYPE)
        page = factory.create_page(args.page_id)
        wordfrequency = factory.create_word_frequency(page.get_page_text(), args.n)
        wordfrequencyoutput = factory.create_word_frequency_output(wordfrequency.top_words(), args.n)

        #print the format of the top words after we count all the words in the wiki page
        print(wordfrequencyoutput.format())

    except WikiException as exp:
        cprint("Exception {}. Exiting".format(str(exp)), "red")
        LOGGER.fatal("Exception {}. Exiting".format(str(exp)))
        sys.exit(1)
if __name__ == '__main__':

    logging.basicConfig(filename="wiki.log",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    main()
