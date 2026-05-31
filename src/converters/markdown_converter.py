import html2text
from src.utils.logger import logger

class MarkdownConverter:

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.body_width = 0