from wordfrequency.wikipage import get_page_text
from wordfrequency.wordfrequency import count_words,top_words,format
import argparse
import sys
from termcolor import cprint
from wordfrequency.exception import WikiException
import logging
import logging.config

logger = logging.getLogger(__name__)

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
    logger.info("Parsing Arguments")
    parser = argparse.ArgumentParser()
    parser.add_argument('--page_id', help='Wiki Page ID', required=True)
    parser.add_argument('--n', help='Top n item to return. Defaults to 5.', required=False)
    parsed_args = parser.parse_args(args)

    if parsed_args.n is None:
        parsed_args.n = 5

    logger.debug("Arguments {}".format(parsed_args))
    return parsed_args

def main():
    """
    Entry Point to Top Wiki Page Word Frequency Counter.
    """
    try:
        #Parse command line args
        args = parse_args(sys.argv[1:])
        #print the format of the top words after we count all the words in the wiki page
        print(format(top_words(count_words(get_page_text(args.page_id)),int(args.n)), args.n))
    except WikiException as exp:
        cprint("Exception {}. Exiting".format(str(exp)), "red")
        logger.fatal("Exception {}. Exiting".format(str(exp)))
        sys.exit(1)
if __name__ == '__main__':

    logging.basicConfig(filename="wiki.log",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    main()
