from configparser import ConfigParser

class ConfigManager:
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_config_value(self, section, option):
        return self.config.get(section, option)
