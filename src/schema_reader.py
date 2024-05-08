import json
import os
import logging
import sys

class SchemaReader:
    """
    Reads the data schema from a file or string.
    Provides methods to retrieve the parsed schema.

    Attributes:
        data_schema (str): The data schema provided as a file path or a JSON string.

    Methods:
        read_schema: Reads and parses the data schema from either a file or a string.
        _read_schema_from_file: Reads the data schema from a file.
        _parse_schema_from_string: Parses the data schema from a JSON string.

    Example:
        data_schema = '{"name": "string", "age": "int", "city": "string"}'
        schema_reader = SchemaReader(data_schema)
        schema = schema_reader.read_schema()
    """

    def __init__(self, data_schema):
        self.data_schema = data_schema

    def read_schema(self):
        if os.path.isfile(f"{os.getcwd()}{self.data_schema}"):
            return self._read_schema_from_file()
        else:
            return self._parse_schema_from_string()

    def _read_schema_from_file(self):
        try:
            with open( f"{os.getcwd()}{self.data_schema}", 'r') as file:
                schema = json.load(file)
            return schema
        except Exception as e:
            logging.error(f"Error reading schema from file: {e}")
            sys.exit(1)

    def _parse_schema_from_string(self):
        try:
            schema = json.loads(self.data_schema)
            return schema
        except Exception as e:
            logging.error(f"Error parsing schema from string: {e}")
            sys.exit(1)
