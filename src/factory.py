from src.arg_parser import ArgParser
from src.config_manager import ConfigManager
from src.arg_manager import ArgManager
from src.arg_processor import ArgProcessor
from src.schema_reader import SchemaReader
from src.data_generator import DataGenerator
from src.file_handler import FileHandler
import logging

logging.getLogger().setLevel(logging.INFO)

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Factory:
    """
    A factory class for creating objects dynamically based on keys.
    This class provides a mechanism for registering and creating objects based on a key.

    Attributes:
        _factories (dict): A dictionary to hold factory functions.

    Methods:
        register: Registers a factory function for a given key.
        create: Creates an object using the registered factory function for the specified key.
    """
    
    _factories = {}

    @classmethod
    def register(cls, key):
        def decorator(func):
            cls._factories[key] = func
            return func
        return decorator

    @classmethod
    def create(cls, key, *args, **kwargs):
        if key in cls._factories:
            return cls._factories[key](*args, **kwargs)
        else:
            raise ValueError(f"No factory registered for key: {key}")

@Factory.register("arg_parser")
def create_arg_parser():
    return ArgParser()

@Factory.register("config_manager")
def create_config_manager(config_file):
    return ConfigManager(config_file)

@Factory.register("arg_manager")
def create_arg_manager(args):
    return ArgManager(args)

@Factory.register("arg_processor")
def create_arg_processor(args):
    return ArgProcessor(args)

@Factory.register("schema_reader")
def create_schema_reader(data_schema):
    return SchemaReader(data_schema)

@Factory.register("data_generator")
def create_data_generator(schema, strategy):
    return DataGenerator(schema, strategy)

@Factory.register("file_handler")
def create_file_handler(args_dict, data_generator):
    return FileHandler(args_dict, data_generator)