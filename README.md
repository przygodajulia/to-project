# JSON Data Generator App

## Description

The JSON Data Generator App is a command-line interface (CLI) utility designed to generate JSON data. It's particularly useful for data engineering tasks such as testing various pipeline flows.

## Usage and Options

### Running the Application
To run the application, use the following command:

python/python3 app.py


### Options

- **Output Directory**: Specifies the directory where generated files will be saved. Defaults to the current directory (`'.'`).

- **File Count**: Specifies the number of files to be generated. Must be greater than 0.

- **File Name**: Specifies the common name shared by all generated files.

- **Strategy**: Specifies the strategy for data generation. Currently supported strategies include:
  - `random`: Generates random integers from 1 to 1000, timestamps, and random strings based on UUID.
  - `sequential`: Generates sequential integers, timestamps, and random strings based on UUID.
  - `fixed`: Generates fixed integer values, timestamps, and random strings based on UUID.

- **Data Schema**: Specifies the schema for the generated data. Supports either a JSON string or a path to a file containing the schema definition. Currently supported data types include:
  - `int`
  - `str`
  - `timestamp`

- **Data Lines**: Specifies the number of lines per file to be generated.

- **Clear Path**: Specifies whether the contents of the output directory should be cleared before writing the files. Options are `True` or `False`.

- **Multiprocessing**: Specifies the number of processors to be used when dealing with larger files.

## Sample Usage

```bash
python3 app.py output --file_count 10 --file_name output --strategy random --data_schema '{"process_id": "int", "process_code": "str", "date_added": "timestamp"}' --data_lines 10 --multiprocessing 1
```

```bash
python3 app.py output --file_count 100 --file_name test --strategy sequential --data_schema '{"process_id": "int", "process_code": "str", "date_added": "timestamp"}' --data_lines 10 --multiprocessing 4
```