import pytest
from unittest.mock import MagicMock, patch
import os
import sys
import json
sys.path.append(os.getcwd())
sys.path.append('/Users/juliaprzygoda/Desktop/to-project-repo/to-project')
from src.file_handler import FileHandler

@pytest.fixture
def file_handler_args():
    return {
        'file_path': '.',
        'file_count': 3,
        'file_name': 'file_test',
        'data_lines': 1
    }

@pytest.fixture
def file_handler_args_absolute():
    return {
        'file_path': '/absolute/path',
        'file_count': 3,
        'file_name': 'file_test',
        'data_lines': 1
    }

@pytest.fixture
def file_handler_args_relative():
    return {
        'file_path': 'relative/path',
        'file_count': 3,
        'file_name': 'file_test',
        'data_lines': 1
    }

@pytest.fixture
def file_handler_dir_to_clear():
    return {
        'file_path': f'{os.getcwd()}/to-project/test/test_output/',
        'file_count': 3,
        'file_name': 'file_test',
        'data_lines': 1
    }

@pytest.fixture
def data_generator():
    return MagicMock()

def test_get_output_path_current_directory(file_handler_args):
    file_handler = FileHandler(file_handler_args, MagicMock())
    assert file_handler.get_output_path() == os.getcwd()

def test_get_output_path_absolute_path(file_handler_args_absolute):
    FileHandler.reset()
    file_handler = FileHandler(file_handler_args_absolute, MagicMock())
    assert file_handler.get_output_path() == '/absolute/path'

def test_get_output_path_relative_path(file_handler_args_relative):
    FileHandler.reset()
    file_handler = FileHandler(file_handler_args_relative, MagicMock())
    assert file_handler.get_output_path() == os.path.join(os.getcwd(), 'relative/path')

def test_clear_directory(file_handler_dir_to_clear):
    FileHandler.reset()
    file_handler = FileHandler(file_handler_dir_to_clear, MagicMock())
    test_path = file_handler.output_path
    print(test_path)

    with open(f"{test_path}test.json", 'w') as opened_file:
        file_data = {'test': 'data'}
        json.dump(file_data, opened_file)

    file_handler.clear_directory("test.json")
    assert len(os.listdir(test_path)) == 0


def test_write_to_file(file_handler_args, data_generator):
    FileHandler.reset()
    file_handler = FileHandler(file_handler_args, data_generator)
    file_handler.output_path = os.getcwd()
    file_data = {'test': 'data'}
    file_name = 'test_file.json'
    file_handler.write_to_file(file_data, file_name)

    with open(f'{os.getcwd()}/{file_name}', 'r') as opened_test_file:
        loaded_file = json.load(opened_test_file)

    assert loaded_file == file_data


@patch('src.file_handler.multiprocessing.Pool')
def test_write_files_multiprocessing_2(mock_pool, file_handler_args, data_generator):
    FileHandler.reset()
    mock_pool_instance = MagicMock()
    mock_pool.return_value = mock_pool_instance
    file_handler = FileHandler(file_handler_args, data_generator)
    file_handler.args_dict["multiprocessing"] = 2
    file_handler.write_files_multiprocessing()

    mock_pool.assert_called_once_with(2)
    