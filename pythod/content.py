from typing import Tuple


class Content(object):
    content_class: str
    target_directory: str
    indicators: Tuple

    def __init__(self, content_class: str, target_directory: str, indicators: Tuple) -> Content:
        self.__content_class = content_class
        self.__indicators = indicators
        self.__target_directory = target_directory

    def get_content_class(self):
        return self.__content_class

    def get_target_directory(self):
        return self.__content_class

    def get_indicators(self):
        return self.__content_class
