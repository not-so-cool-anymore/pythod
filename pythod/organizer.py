from .configuration_deserializer import ConfigurationDeserializer
import os
import shutil


class Organizer():
    def __init__(self, org_directory, configuration_path=None):
        self.__org_directory = org_directory
        self.__configuration_path = configuration_path

    def organize(self):
        configuration = self.__load_configuration()
        self.__build_target_directories(configuration)

        for root, dirs, files in os.walk(self.__org_directory):
            for _dir in dirs:
                target_directory = self.__get_target_directory(
                    configuration,
                    _dir,
                    True
                )

                if target_directory != None:
                    self.__move_object(
                        os.path.join(root, _dir),
                        os.path.join(root, target_directory)
                    )

            for _file in files:
                target_directory = self.__get_target_directory(
                    configuration,
                    _file
                )

                if target_directory != None:
                    self.__move_object(
                        os.path.join(root, _file),
                        os.path.join(root, target_directory)
                    )

            break

    def __move_object(self, source, target):
        shutil.move(source, target)

    def __get_target_directory(self, configuration, element, is_directory=False):
        for content in configuration.contents:
            if not is_directory and element.endswith(content.get_indicators()):
                return content.get_target_directory()
            elif is_directory and any(string in element for string in content.get_indicators()) and content.content_class == 'directory':
                return content.get_target_directory()

        print('>>> Target directory not found for: {}'.format(element))
        return None

    def __build_target_directories(self, configuration):
        for content in configuration.contents:
            if not os.path.isdir(os.path.join(self.__org_directory, content.get_target_directory())):
                os.mkdir(os.path.join(
                    self.__org_directory,
                    content.get_target_directory()
                ))

                print('>>> Created content directory {}.'.format(
                    os.path.join(self.__org_directory,
                                 content.get_target_directory())
                ))

    def __load_configuration(self):
        if self.__configuration_path == None:
            current_dir = self.__get_current_directory_path()

            self.__configuration_path = os.path.join(
                current_dir, 'config.json')

        deserializer = ConfigurationDeserializer(self.__configuration_path)
        configuration = deserializer.deserialize()

        return configuration

    def __get_current_directory_path(self):
        return os.path.dirname(os.path.abspath(__file__))
