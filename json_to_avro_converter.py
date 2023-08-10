# from fastavro import json_reader, writer, reader, parse_schema, schemaless_writer
from schema import SCHEMA
import json
import argparse
import time
from tqdm import tqdm
import fastavro


OUTPUT_FILE = "records.avro"
# To ensure the correct schema for your data in the schema file,
# please refer to this link: https://konbert.com/
# Choose "json to avro" and check the option "only schema".

def read_json_file(path_to_json) -> list[dict]:
    """
    Reads a JSON file and returns its contents as a list of dictionaries.

    Args:
    - path_to_json: A string representing the path to the JSON file to be read.

    Returns:
    - A list of dictionaries representing the JSON data.

    Raises:
    - FileNotFoundError: If the specified JSON file does not exist.
    - JSONDecodeError: If the JSON file is not valid and cannot be decoded.

    Example Usage:
    ```python
    json_file_name = "data.json"
    records = read_json_file(json_file_name)
    print(records)
    ```
    """

    with open(path_to_json, 'r', encoding='utf-8') as file:
        records = [json.loads(each_line) for each_line in file]
    print("------> JSON LOADED")
    return records    

def write_to_avro(avro_file_name, json_file_name, schema=SCHEMA) -> None:
    """
    Write data in Avro format to a file.

    This function takes in three parameters: avro_file_name, json_file_name, and schema.
    It reads data from a JSON file, converts it to Avro format, and writes it to a new Avro file specified by avro_file_name.
    The Avro schema is provided by the schema parameter.

    Args:
        avro_file_name (str): The name of the file to write to.
        json_file_name (str): The name of the JSON file to read from.
        schema (Avro schema object, optional): The Avro schema object. Default is SCHEMA.

    Returns:
        None

    Raises:
        FileNotFoundError: If the JSON file specified by json_file_name is not found.
    """
    try:
        schema_separated_parsed = fastavro.parse_schema(schema)
        records = read_json_file(json_file_name)
        with open(avro_file_name, 'wb') as f:
            fastavro.writer(f, schema_separated_parsed, records)
        f.close()
        print(f"------> {avro_file_name} CREATED")
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        
    except PermissionError as e:
        print(f"Error: Permission denied - {e}")
        
    except fastavro.schema.SchemaParseException as e:
        print(f"Error: Schema parsing error - {e}")



def main():
    """
    Converts a JSON file to an Avro file.

    This function takes command line arguments for the input JSON file and the output Avro file.
    It uses the argparse module to parse the command line arguments and the time module to measure the execution time.
    The function calls another function write_to_avro to perform the actual conversion.
    The execution time is printed at the end.
    """

    parser = argparse.ArgumentParser(description='This file convert json file to avro')
    add_arg = parser.add_argument

    requiredNamed = parser.add_argument_group('required arguments')
    
    requiredNamed.add_argument('-i', dest='input_file', type=str, help="the path to the input json file", required=True )
    
    add_arg('-o', dest='output_file', type=str, default=OUTPUT_FILE, help="the path to the OUTPUT avro file, default value %s" %OUTPUT_FILE)

    args = parser.parse_args()
    # Computing execution time
    start = time.time()
    
    write_to_avro(args.output_file, args.input_file)

    end = time.time()
    print("The time of execution :", (end-start) *10**3," ms")



if __name__=='__main__':
    main()
