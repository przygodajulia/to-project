import os
import logging
import math
import random
import uuid
import multiprocessing
import json

logging.getLogger().setLevel(logging.INFO)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FileHandler(metaclass=SingletonMeta):
    """Singleton class for handling file operations."""

    def __init__(self, args_dict, data_generator):
        self.args_dict = args_dict
        self.data_generator = data_generator
        self.output_path = self.get_output_path()

    def get_output_path(self):
        """Retrieve the output path from the args_dict."""
        file_path = self.args_dict.get('file_path', '.')
        if file_path == '.':
            output_dir_path = os.getcwd()
        elif file_path.startswith('/'):
            output_dir_path = file_path
        else:
            output_dir_path = os.path.join(os.getcwd(), file_path)

        return output_dir_path

    def clear_directory(self, file_name):
        """Clear files with the same name in output directory."""
        for file in os.listdir(self.output_path):
            if file.startswith(file_name):
                file_to_delete = os.path.join(self.output_path, file)
                os.remove(file_to_delete)

    def write_to_file(self, data, file_name):
        """Write data to a file."""
        file_path = os.path.join(self.output_path, file_name)
        with open(file_path, "w") as file:
            json.dump(data, file)

    def create_files(self):
        """Helper function to create files while using multiprocessing."""
        num_files = self.args_dict["file_count"]
        file_name = self.args_dict["file_name"]
        data_lines = self.args_dict["data_lines"]

        for i in range(num_files):
            prefix_value = i

            file_data = []
            for j in range(data_lines):
                line = self.data_generator.generate_data()
                file_data.append(line)

            self.write_to_file(file_data, f"{file_name}{prefix_value}.json")

    def write_files_multiprocessing(self):
        """Write files using multiprocessing."""
       
        multiprocessing_count = self.args_dict.get("multiprocessing", 1)
        
        if multiprocessing_count > 1:
            with multiprocessing.Pool(multiprocessing_count) as pool:
                tasks = []
                for _ in range(self.args_dict["file_count"]):
                    tasks.append(pool.apply_async(self.create_files, ()))

                for task in tasks:
                    task.get()
        else:
            self.create_files()

        logging.info("Generating files finished")

    @classmethod
    def reset(cls):
        cls._instances = {}

