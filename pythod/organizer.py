from .configuration_deserializer import ConfigurationDeserializer
import os
import shutil


class Organizer():
    def __init__(self, org_directory, configuration_path=None):
        self.__org_directory = org_directory
        self.__configuration_path = configuration_path

    def organize(self):
        configuration = self.__load_configuration()

        for root, dirs, files in os.walk(self.__org_directory):
            for _dir in dirs:
                target_directory = self.__get_target_directory(
                    configuration,
                    _dir,
                    True
                )

                self.__move_object(
                    os.path.join(self.__org_directory, _dir),
                    os.path.join(self.__org_directory, target_directory)
                )

            for _file in files:
                target_directory = self.__get_target_directory(
                    configuration,
                    _file
                )

                self.__move_object(
                    os.path.join(self.__org_directory, _file),
                    os.path.join(self.__org_directory, target_directory)
                )

    def __move_object(self, source, target):
        shutil.move(source, target)

    def __get_target_directory(self, configuration, element, is_directory=False):
        for content in configuration:
            if not is_directory and element.endswith(content.get_indicators()):
                return content.get_target_directory()
            elif is_directory and any(string in element for string in content.get_indicators()):
                return content.get_target_directory()

        print('>>> Target directory not found for: {}'.format(element))

    def __build_target_directories(self, configuration):
        for content in configuration:
            print('>>> Content class {} will use directory {}.'.format(
                content.get_content_class(),
                content.get_target_directory()
            ))

            if not os.path.isdir(content.get_target_directory()):
                os.mkdir(os.path.join(
                    self.__org_directory,
                    content.get_target_directory()
                ))

    def __load_configuration(self):
        if self.__configuration_path == None:
            self.__configuration_path = './config.json'

        deserializer = ConfigurationDeserializer(self.__configuration_path)
        configuration = deserializer.deserialize()

        return configuration
