import argparse

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="data_generator", description="Collect arguments provided in the command-line.")

    def add_arguments(self):
        self.parser.add_argument("file_path", help="Provide path to an existing directory")
        self.parser.add_argument("--file_count", help="Number of files to be created, default 0 prints data in the console",
                                  type=int)
        self.parser.add_argument("--file_name", help="Default name: file", type=str)
        self.parser.add_argument("--file_prefix", help="Choose an option to create file prefixes",
                                  choices=["count", "random", "uuid"])
        self.parser.add_argument("--strategy", help="Choose an option to generate files",
                                  choices=["random", "sequential", "fixed"])
        self.parser.add_argument("--data_schema", help="Provide data schema either in terminal or path to file")
        self.parser.add_argument("--data_lines", help="Specify how many lines should be generated", type=int)
        self.parser.add_argument("--clear_path", help="If flag is on all files with the same name file name and in the same "
                                  "directory will be removed", action="store_true")
        self.parser.add_argument("--multiprocessing", help="Define how many processors should be used to generate file",
                                  type=int)