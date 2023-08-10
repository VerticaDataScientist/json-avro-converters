from fastavro import reader, json_writer
import time
import argparse



OUTPUT_FILE_NAME = "json_file.json"

def main():
    """
    Converts a JSON file to an Avro file.

    This function takes the input JSON file path and the output Avro file path as command line arguments.
    It uses the `fastavro` library to read the Avro file and write the JSON file.
    The execution time of the conversion is also calculated and printed.

    Example Usage:
    python script.py -i input.json -o output.avro
    """

    parser = argparse.ArgumentParser(description='This file convert json file to avro')
    add_arg = parser.add_argument

    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument('-i', dest='input_file', type=str, help="the path to the input json file", required=True )
    
    add_arg('-o', dest='output_file_name', type=str, 
            default=OUTPUT_FILE_NAME, 
            help="the path to the output json file, default value %s" %OUTPUT_FILE_NAME)

    args = parser.parse_args()

    # Computing execution time
    start = time.time()

    with open(args.output_file_name, "w") as json_file:
        with open(args.input_file_name, "rb") as avro_file:
            avro_reader = reader(avro_file)
            json_writer(json_file, avro_reader.writer_schema, avro_reader)
        avro_file.close()
    json_file.close()
    end = time.time()   
    print(f"------> {args.output_file_name} CREATED")
    print("The time of execution :", (end-start) *10**3," ms")


if __name__=="__main__":
    main()