import random
import time
import uuid

class DataGenerator:
    """
    A class for generating data based on a specified schema and strategy.

    Attributes:
        schema (str): The data schema used for generating data.
        strategy (str): The generation strategy to be applied.
        increment_val (int): Value used for sequential data generation.

    Methods:
        generate_data: Generates data based on the specified schema and strategy.
        _get_strategy: Retrieves the appropriate strategy.

    Example:
        schema = '{"name": "str", "age": "int", "city": "str"}'
        strategy = 'random'
        data_generator = DataGenerator(schema, strategy)
        generated_data = data_generator.generate_data()
    """

    def __init__(self, schema, strategy):
        self.schema = schema
        self.strategy = strategy
        self.increment_val = 0

    def generate_data(self):
        strategy = self._get_strategy()
        return strategy.generate()

    def _get_strategy(self):
        if self.strategy == "random":
            return RandomDataStrategy(self.schema)
        elif self.strategy == "sequential":
            self.increment_val += 1
            return SequentialDataStrategy(self.schema, self.increment_val)
        elif self.strategy == "fixed":
            return FixedValueDataStrategy(self.schema)

class BaseDataStrategy:
    """Base class for data generation strategies."""

    def __init__(self, schema):
        self.schema = schema

    def generate(self):
        raise NotImplementedError("generate method must be implemented in subclasses")

class RandomDataStrategy(BaseDataStrategy):
    """Generate data randomly based on the schema."""

    def generate(self):
        data = {}
        for key, value in self.schema.items():
            data[key] = self._generate_value(value)
        return data

    def _generate_value(self, data_type):
        if data_type == "timestamp":
            return str(time.time())
        elif data_type == "int":
            return random.randint(1, 1000)
        elif data_type == "str":
            return str(uuid.uuid4())

class SequentialDataStrategy(BaseDataStrategy):
    """Generate data sequentially based on the schema."""

    def __init__(self, schema, current_value):
        super().__init__(schema)
        self.current_value = current_value

    def generate(self):
        data = {}
        for key, value in self.schema.items():
            data[key] = self._generate_value(value)
        return data

    def _generate_value(self, data_type):
        if data_type == "timestamp":
            return str(time.time() + self.current_value)
        elif data_type == "int":
            return self.current_value
        elif data_type == "str":
            return str(uuid.uuid4())
        


class FixedValueDataStrategy(BaseDataStrategy):
    """Generate data with fixed values for integer fields."""

    def __init__(self, schema):
        super().__init__(schema)
        self.current_value = 1

    def generate(self):
        data = {}
        for key, value in self.schema.items():
            data[key] = self._generate_value(value)
        return data

    def _generate_value(self, data_type):
        if data_type == "timestamp":
            return str(time.time())
        elif data_type == "int":
            return self.current_value
        elif data_type == "str":
            return str(uuid.uuid4())

 

