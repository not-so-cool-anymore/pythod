import json
from .configuration import Configuration
from .content import Content


class ConfigurationDeserializer(object):
    def __init__(self, configuration_file_location):
        self.__configuration_file_location = configuration_file_location

    def deserialize(self) -> Configuration:
        configuration_file_contents = self.__read_configuration_file()
        configuration_json = json.loads(configuration_file_contents)

        configuration = self.__decode_configuration(configuration_json)

        return configuration

    def __decode_configuration(self, configuration_json) -> Configuration:
        contents = list()
        if 'contents' in configuration_json:
            for content in configuration_json['contents']:
                _content = Content(
                    content['content_class'],
                    tuple(content['indicators']),
                    content['target_directory']
                )

                contents.append(_content)

        return Configuration(contents)

    def __read_configuration_file(self) -> str:
        with open(self.__configuration_file_location) as configuration_file:
            return configuration_file.read()
