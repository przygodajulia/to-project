from configparser import ConfigParser

class ConfigManager:
    """
    A class for managing configuration values from a config file.

    Attributes:
        config (ConfigParser): A ConfigParser object for parsing the config file.

    Methods:
        get_config_value: Retrieves a configuration value from the specified section and option.

    Example:
        config_file = 'config.ini'
        config_manager = ConfigManager(config_file)
        value = config_manager.get_config_value('Section', 'Option')
    """
    
    def __init__(self, config_file):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_config_value(self, section, option):
        return self.config.get(section, option)
