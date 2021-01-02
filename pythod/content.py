from typing import Tuple


class Content(object):
    content_class: str
    target_directory: str
    indicators: Tuple

    def __init__(self, content_class: str, indicators: Tuple, target_directory: str):
        self.content_class = content_class
        self.indicators = indicators
        self.target_directory = target_directory

    def get_content_class(self):
        return self.content_class

    def get_target_directory(self):
        return self.target_directory

    def get_indicators(self):
        return self.indicators
