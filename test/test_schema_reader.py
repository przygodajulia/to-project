import pytest
import os
import sys
sys.path.append(os.getcwd())
from src.schema_reader import SchemaReader

@pytest.fixture
def schema_reader_from_str_valid():
    schema = '{"name": "str", "age": "int", "date_added": "timestamp"}'
    return SchemaReader(schema)

@pytest.fixture
def schema_reader_from_str_invalid():
    schema = 'name, float'
    return SchemaReader(schema)

@pytest.fixture
def schema_reader_from_file():
    schema_path = '/to-project/test/test_input/test_schema.json'
    return SchemaReader(schema_path)

@pytest.fixture
def schema_reader_from_file_invalid():
    schema_path = 'invalid_path'
    return SchemaReader(schema_path)

def test_read_schema_from_string(schema_reader_from_str_valid):
    read_schema = schema_reader_from_str_valid.read_schema()
    assert read_schema == {'name': 'str', 'age': 'int', 'date_added': 'timestamp'}

def test_read_schema_from_string_invalid(schema_reader_from_str_invalid):
    with pytest.raises(SystemExit):
        schema_reader_from_str_invalid.read_schema()

def test_read_schema_from_file(schema_reader_from_file):
    read_schema = schema_reader_from_file.read_schema()
    assert read_schema == {'name': 'str', 'age': 'int', 'date_added': 'timestamp'}

def test_read_schema_from_file_invalid(schema_reader_from_file_invalid):
    with pytest.raises(SystemExit):
        schema_reader_from_file_invalid.read_schema()