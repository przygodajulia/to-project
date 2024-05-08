from src.factory import Factory
from src.timer import ExecutionTimeDecorator
import logging
import os

logging.getLogger().setLevel(logging.INFO)


@ExecutionTimeDecorator
def app():
    arg_parser = Factory.create("arg_parser")
    arg_parser.add_arguments()
    args = arg_parser.parser.parse_args()

    config_manager = Factory.create("config_manager", "default.ini")

    argument_manager = Factory.create("arg_manager", args)
    argument_manager.file_path = args.file_path or config_manager.get_config_value("DEFAULT", "file_path")
    argument_manager.file_count = args.file_count or config_manager.get_config_value("DEFAULT", "file_count")
    argument_manager.file_name = args.file_name or config_manager.get_config_value("DEFAULT", "file_name")
    argument_manager.strategy = args.strategy or config_manager.get_config_value("DEFAULT", "strategy")
    argument_manager.data_lines = args.data_lines or config_manager.get_config_value("DEFAULT", "data_lines")
    argument_manager.multiprocessing = args.multiprocessing or config_manager.get_config_value("DEFAULT", "multiprocessing")

    collected_args = argument_manager.__dict__
    print(" >> Arguments collected:")
    print(collected_args)
    print()

    arg_processor = Factory.create("arg_processor", collected_args)
    arg_processor.process_arguments()
    arg_processor_validated = arg_processor.get_validated_args()
    print(" >> Arguments validated:")
    print(arg_processor_validated)
    print()

    schema_reader = Factory.create("schema_reader", arg_processor_validated["data_schema"])
    data_schema = schema_reader.read_schema()

    data_generator = Factory.create("data_generator", data_schema, arg_processor_validated["strategy"])

    file_handler = Factory.create("file_handler", arg_processor_validated, data_generator)
    file_handler.write_files_multiprocessing()

if __name__ == "__main__":
    app()
