class ArgManager:
    """
    A class for managing command-line arguments related to data generation.
    Accepts an argparse.Namespace object containing parsed command-line arguments
    and extracts relevant attributes.

    Attributes:
        file_path (str): Path to an existing directory where files will be generated or current directory.
        file_count (int): Number of files to be created.
        file_name (str): Name template for generated files.
        strategy (str): Generation strategy for the files, chosen from ["random", "sequential", "fixed"].
        data_schema (str): Data schema either provided directly or as a path to a schema file.
        data_lines (int): Number of lines to be generated in each file.
        clear_path (bool): Flag indicating whether to remove existing files with the same name in the same directory.
        multiprocessing (int): Number of processors to be used for file generation.

    Example:
        args = arg_parser.parser.parse_args()
        arg_manager = ArgManager(args)
        file_path = arg_manager.file_path
    """

    def __init__(self, args):
        self.file_path = args.file_path
        self.file_count = args.file_count
        self.file_name = args.file_name
        self.strategy = args.strategy
        self.data_schema = args.data_schema
        self.data_lines = args.data_lines
        self.clear_path = args.clear_path
        self.multiprocessing = args.multiprocessing
