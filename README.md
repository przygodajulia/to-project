# JSON data generator app

- sample usage 
python3 app.py src --file_count 10 --file_name output --file_prefix count --data_schema '''
{   
    "name": "str",
    "age": "int",
    "timestamp": "timestamp",
    "status": "str:rand",
    "category": "str:['A', 'B', 'C']"
}
''' --data_lines 100 --multiprocessing 4

python3 app.py src --file_count 10 --file_name output --file_prefix count --data_schema '''
{"name": "str", "age": "int"}''' --data_lines 100 --multiprocessing 1

