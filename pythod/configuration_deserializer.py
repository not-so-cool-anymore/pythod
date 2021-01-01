import json
from .configuration import Configuration


class ConfigurationDeserializer(object):
    def __init__(self, configuration_file_location):
        self.__configuration_file_location = configuration_file_location

    def deserialize(self) -> Configuration:
        configuration_file_contents = self.__read_configuration_file()
        configuration_json = json.loads(configuration_file_contents)

        return Configuration(**configuration_json)

    def __read_configuration_file(self) -> str:
        with open(self.__configuration_file_location) as configuration_file:
            return configuration_file.read()
