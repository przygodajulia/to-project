class ArgManager:
    def __init__(self, args):
        self.file_path = args.file_path
        self.file_count = args.file_count
        self.file_name = args.file_name
        self.file_prefix = args.file_prefix
        self.strategy = args.strategy
        self.data_schema = args.data_schema
        self.data_lines = args.data_lines
        self.clear_path = args.clear_path
        self.multiprocessing = args.multiprocessing
