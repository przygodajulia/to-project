import pytest
import logging
import os
import sys
sys.path.append('/Users/juliaprzygoda/Desktop/to-project-repo/to-project') #TODO
from src.schema_reader import SchemaReader

@pytest.fixture
def schema_reader_from_str():
    schema = '{"name": "str", "age": "int", "date_added": "timestamp"}'
    return SchemaReader(schema)


@pytest.fixture
def schema_reader_from_file():
    schema_path = 'todo'
    return SchemaReader(schema_path)

def test_read_schema_from_string(schema_reader_from_str):
    read_schema = schema_reader_from_str.read_schema()
    assert read_schema == {'name': 'str', 'age': 'int', 'date_added': 'timestamp'}