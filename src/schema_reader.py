import json
import os
import logging
import sys

class SchemaReader:
    """
    Reads the data schema from a file or string.
    Provides methods to retrieve the parsed schema.
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
