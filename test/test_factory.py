import pytest
from argparse import Namespace
import os
import sys
sys.path.append(os.getcwd())
from src.factory import Factory
from src.arg_parser import ArgParser
from src.config_manager import ConfigManager
from src.arg_manager import ArgManager
from src.arg_processor import ArgProcessor
from src.schema_reader import SchemaReader
from src.data_generator import DataGenerator

ARGS = Namespace(
    file_path="/path/to/your/file",
    file_count=5,
    file_name="example.txt",
    strategy="your_strategy",
    data_schema="your_data_schema",
    data_lines=100,
    clear_path="/path/to/clear",
    multiprocessing=True
)

ARGS_DICT = {
        'file_path': 'relative/path',
        'file_count': 3,
        'file_name': 'file_test',
        'data_lines': 1
    }

DATA_SCHEMA = '{"name": "str", "age": "int", "date_added": "timestamp"}'

@pytest.fixture
def arg_parser_factory():
    return Factory.create("arg_parser")

@pytest.fixture
def config_manager_factory():
    return Factory.create("config_manager", "config_file_path")

@pytest.fixture
def arg_manager_factory():
    return Factory.create("arg_manager", ARGS)

@pytest.fixture
def arg_processor_factory():
    return Factory.create("arg_processor", ARGS)

@pytest.fixture
def schema_reader_factory():
    return Factory.create("schema_reader", DATA_SCHEMA)

@pytest.fixture
def data_generator_factory():
    return Factory.create("data_generator", DATA_SCHEMA, 'random')

def test_create_arg_parser(arg_parser_factory):
    assert isinstance(arg_parser_factory, ArgParser)

def test_create_config_manager(config_manager_factory):
    assert isinstance(config_manager_factory, ConfigManager)

def test_create_arg_manager(arg_manager_factory):
    assert isinstance(arg_manager_factory, ArgManager)

def test_create_arg_processor(arg_processor_factory):
    assert isinstance(arg_processor_factory, ArgProcessor)

def test_create_schema_reader(schema_reader_factory):
    assert isinstance(schema_reader_factory, SchemaReader)

def test_create_data_generator(data_generator_factory):
    assert isinstance(data_generator_factory, DataGenerator)

def test_create_invalid_factory():
    with pytest.raises(ValueError):
        Factory.create("invalid_key")
