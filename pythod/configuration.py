from typing import List
from .content import Content


class Configuration(object):
    contents: List[Content]

    def __init__(self, contents: List[Content]):
        self.__contents = contents

    def __str__(self) -> str:
        contents_layout = ''

        for content in self.__contents:
            contents_layout += 'Content class: {}\nTarget folder:{}\nContent class indicators:\n'.format(
                content.get_content_class(),
                content.get_target_folder()
            )

            for indicator in content.get_indicators():
                contents_layout += '\t{}'.format(indicator)

        return contents_layout
