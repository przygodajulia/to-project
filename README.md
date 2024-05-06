### JSON data generator app

# Description
This tool is a command-line interface (CLI) utility designed for generating JSON data, that can be useful for data engineering tasks such as testing different pipeline flows.


# Usage and different options 
python3 app.py 

+ output directory ['.', 'path_to_some_dir'] - . will use current directory
+ file count - how many files will be generated, needs to be greater than 0
+ file name - name all generated files will share
+ strategy - ['random', 'sequential', 'fixed']
    currently supported strategy types
    - random 
        - generates random integers from 1 to 1000
        - generates timestamps
        - generates random str based on uuid
    - sequential
        - generates sequential integers
        - generates timestamps
        - generates random str based on uuid
    - fixed
        - generates fixed integer values
        - generates timestamps
        - generates random str based on uuid
+ data_schema = ['json_str', 'path_to_file']
    currently supported data types
    - int
    - str
    - timestamp
+ data_lines - how many lines per each file should be generated
+ clear_path - [True, False] - whether the contents of outout directory should be cleared before writing the files
+ multiprocessing - when dealing with larger files, specify how many processors should be used


# Sample usage 
python3 app.py output --file_count 2 --file_name output --strategy sequential --data_schema '''{"name": "str", "age": "int", "date_added": "timestamp"}''' --data_lines 10 --multiprocessing 1

will generate in 2 files each having 10 lines 

# Design patterns
- SOLID
- Singleton using Metaclass
- Strategy
- Decorator -> to measure execution of the whole flow
- Factory


# Project structure and components

# Tests