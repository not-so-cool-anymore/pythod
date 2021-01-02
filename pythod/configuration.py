from typing import List
from .content import Content


class Configuration(object):
    contents: List[Content]

    def __init__(self, contents: List[Content]):
        self.contents = contents

    def get_contents(self):
        return self.contents

    def __str__(self) -> str:
        contents_layout = ''

        for content in self.contents:
            contents_layout += 'Content class: {}\nTarget folder: {}\nContent class indicators:\n'.format(
                content.get_content_class(),
                content.get_target_directory()
            )

            for indicator in content.get_indicators():
                contents_layout += '\t{}\n'.format(indicator)
            contents_layout += '-'*30+'\n'
        return contents_layout
