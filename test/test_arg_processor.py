import pytest
import logging
import os
import sys
sys.path.append('/Users/juliaprzygoda/Desktop/to-project-repo/to-project') #TODO
from src.arg_processor import ArgProcessor

@pytest.fixture
def arg_parser_valid():
    mock_dict = {
        'file_path': '.',
        'file_count': 3,
        'file_name': 'file_test',
        'strategy': 'random',
        'data_schema': "{'test': 'int'}",
        'data_lines': 1,
        'multiprocessing': 1
    }
    return ArgProcessor(mock_dict)

@pytest.fixture
def arg_parser_invalid():
    mock_dict = {
        'file_path': 'invalid_directory',
        'file_count': -3,
        'file_name': 'file_test',
        'strategy': 'invalid_strategy',
        'data_schema': "{'test': 'int'}",
        'data_lines': -1,
        'multiprocessing': -1
    }
    return ArgProcessor(mock_dict)

def test_valid_file_path(arg_parser_valid):
    arg_parser_valid._validate_file_path()

def test_invalid_file_path(arg_parser_invalid):
    with pytest.raises(SystemExit):
        arg_parser_invalid._validate_file_path()

def test_valid_file_count(arg_parser_valid):
    arg_parser_valid._validate_file_count()

def test_invalid_file_count(arg_parser_invalid):
    with pytest.raises(SystemExit):
        arg_parser_invalid._validate_file_count()

def test_valid_data_lines(arg_parser_valid):
    arg_parser_valid._validate_line_count()

def test_invalid_data_lines(arg_parser_invalid):
    with pytest.raises(SystemExit):
        arg_parser_invalid._validate_line_count()

def test_valid_multiprocessing_count(arg_parser_valid):
    arg_parser_valid._validate_multiprocessing()

def test_invalid_multiprocessing_count(arg_parser_invalid):
    with pytest.raises(SystemExit):
        arg_parser_invalid._validate_multiprocessing()

def test_valid_strategy(arg_parser_valid):
    arg_parser_valid._validate_strategy()

def test_invalid_multiprocessing_count(arg_parser_invalid):
    with pytest.raises(SystemExit):
        arg_parser_invalid._validate_strategy()
