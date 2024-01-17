from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder, Footer, Header, Markdown, Tree
from textual.binding import Binding
import argparse
import logging

logging.basicConfig(filename='browser.log', filemode ='a', format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')


NAVIGATION = [{}]
CURRENT = NAVIGATION[0]

tree: Tree[dict] = Tree("Home", id='nav')

def populate(path):
    logging.info("populate started")
    pass

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info("Browser started")
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path for docs")
    args = parser.parse_args()
    populate(args.path)
    #app = Documentation()
    #app.run()