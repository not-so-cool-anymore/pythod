from json import JSONEncoder


class ConfigurationEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
