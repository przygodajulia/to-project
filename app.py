from src.arg_parser import ArgParser
from src.config_manager import ConfigManager
from src.arg_manager import ArgManager
from src.arg_processor import ArgProcessor
from src.schema_reader import SchemaReader
from src.data_generator import DataGenerator
from src.file_handler import FileHandler

def main():
    # Read configuration options provided in the command line
    arg_parser = ArgParser()
    arg_parser.add_arguments()
    args = arg_parser.parser.parse_args()

    # If some of the necessary fields where not provided use default configuration file
    config_manager = ConfigManager("default.ini")

    # Combine configuration data from both sources
    argument_manager = ArgManager(args)
    argument_manager.file_path = args.file_path or config_manager.get_config_value("DEFAULT", "file_path")
    argument_manager.file_count = args.file_count or config_manager.get_config_value("DEFAULT", "file_count")
    argument_manager.file_name = args.file_name or config_manager.get_config_value("DEFAULT", "file_name")
    argument_manager.file_prefix = args.file_prefix or config_manager.get_config_value("DEFAULT", "file_prefix")
    argument_manager.strategy = args.strategy or config_manager.get_config_value("DEFAULT", "strategy")
    argument_manager.data_lines = args.data_lines or config_manager.get_config_value("DEFAULT", "data_lines")
    argument_manager.multiprocessing = args.multiprocessing or config_manager.get_config_value("DEFAULT", "multiprocessing")

    collected_args = argument_manager.__dict__
    print("Arguments collected:")
    print(collected_args)

    # Check the values provided by the user
    arg_processor = ArgProcessor(collected_args)
    arg_processor_validated = arg_processor.get_validated_args()
    print("Arguments validated:")
    print(arg_processor_validated)

    # Read schema of the data that is to be generated
    schema_reader = SchemaReader(arg_processor_validated["data_schema"])
    data_schema = schema_reader.read_schema()

    # Initialize data generator and generate data
    data_generator = DataGenerator(data_schema, arg_processor_validated["strategy"])

    # Instantiate FileHandler and write to files
    file_handler = FileHandler(arg_processor_validated, data_generator)
    file_handler.write_files_multiprocessing()



if __name__ == "__main__":
    main()
