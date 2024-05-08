import pytest
import os
import sys
sys.path.append(os.getcwd())
from src.data_generator import DataGenerator, RandomDataStrategy, SequentialDataStrategy, FixedValueDataStrategy

@pytest.fixture
def data_generator_random():
    schema = {"name": "str", "age": "int", "date_added": "timestamp"}
    return DataGenerator(schema, "random")

@pytest.fixture
def data_generator_sequential():
    schema = {"name": "str", "age": "int", "date_added": "timestamp"}
    return DataGenerator(schema, "sequential")

@pytest.fixture
def data_generator_fixed():
    schema = {"name": "str", "age": "int", "date_added": "timestamp"}
    return DataGenerator(schema, "fixed")

def test_generate_data_random(data_generator_random):
    data = data_generator_random.generate_data()
    assert isinstance(data["name"], str)
    assert isinstance(data["age"], int)
    assert isinstance(data["date_added"], str)

def test_generate_data_sequential(data_generator_sequential):
    data = data_generator_sequential.generate_data()
    assert isinstance(data["name"], str)
    assert data["age"] == 1
    assert isinstance(data["date_added"], str)

def test_generate_data_fixed(data_generator_fixed):
    data = data_generator_fixed.generate_data()
    assert isinstance(data["name"], str)
    assert data["age"] == 1
    assert isinstance(data["date_added"], str)

def test_get_strategy_random(data_generator_random):
    strategy = data_generator_random._get_strategy()
    assert isinstance(strategy, RandomDataStrategy)

def test_get_strategy_sequential(data_generator_sequential):
    strategy = data_generator_sequential._get_strategy()
    assert isinstance(strategy, SequentialDataStrategy)

def test_get_strategy_fixed(data_generator_fixed):
    strategy = data_generator_fixed._get_strategy()
    assert isinstance(strategy, FixedValueDataStrategy)
