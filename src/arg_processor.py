import logging
import sys
import os

logging.getLogger().setLevel(logging.INFO)

class ArgProcessor:
    """
        Initialize the argument processing logic and validate the arguments.
        Provide methods to retrieve validated arguments.
    """
    
    def __init__(self, args):
        self.args = args

    def process_arguments(self):
    
        self._validate_file_path()
        self._validate_file_count()
        self._validate_line_count()
        self._validate_strategy()
        self._validate_multiprocessing()

    def _validate_file_path(self):
        file_path = self.args['file_path']
        if file_path == '.':
            self.path = os.getcwd()
        elif file_path.startswith('/'):
            self.path = file_path
        else:
            self.path = os.path.join(os.getcwd(), file_path)

        if not os.path.isdir(self.path):
            logging.error("Specified path is not a directory")
            sys.exit(1)

    def _validate_file_count(self):
        self.file_count = self.args.get("file_count", 0)
        if self.file_count <= 0:
            logging.error("Number of files cannot be a negative value")
            sys.exit()

    def _validate_line_count(self):
        self.data_lines = self.args.get("data_lines", 0)
        if self.data_lines <= 0:
            logging.error("Number of lines cannot be a negative value")
            sys.exit()


    def _validate_multiprocessing(self):
        self.multiprocessing = self.args.get("multiprocessing", os.cpu_count())
        if self.multiprocessing < 0:
            logging.error("Number of processors cannot be a negative value")
            sys.exit()
        elif self.multiprocessing > os.cpu_count():
            self.multiprocessing = os.cpu_count()

    def _validate_strategy(self):
        if self.args["strategy"] not in ["random", "sequential", "fixed"]:
            logging.error("Specified strategy does not exist")
            sys.exit(1)


    def get_file_path(self):
        return self.path

    def get_file_count(self):
        return self.file_count

    def get_multiprocessing(self):
        return self.multiprocessing
    
    def get_validated_args(self):
        return self.args

    def __repr__(self):
        return f"{self.args}"