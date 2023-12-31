# JSON to Avro Conversion Script

This repository contains Python scripts to convert JSON data into Avro format. The conversion is performed by reading a JSON file, parsing its contents, and writing the data to an Avro file. The schema for the Avro data is provided in the `schema.py`.

## Getting Started
Follow the steps below to use the JSON to Avro conversion scripts:

1. Clone the Repository: Clone this repository to your local machine using the following

```bash
git clone https://github.com/VerticaDataScientist/json-acro-convertors.git
```

2. Install Dependencies: The conversion scripts use the fastavro library for Avro operations. Install the required dependencies by running:

```bash
pip install fastavro
```

3. Prepare Your JSON Data: Place the JSON data file you want to convert into the repository directory (each record should be in a separated line - not in a list).

4. Adjust Schema: Open the schema.py file and adjust the SCHEMA dictionary to match the schema of your JSON data. You can also generate the schema using online tools like [Konbert](https://konbert.com/).

5. Run the Conversion Script: Open a terminal and navigate to the repository directory. Run the conversion script using the following command:
```bash
python json_to_avro_converter.py -i input.json -o output.avro
```
Replace input.json with the name of your JSON file and output.avro with the desired name for the output Avro file.

6. Check Output: After running the script, you will find the converted Avro file in the repository directory.

### Command Line Arguments

The conversion script supports the following command line arguments:

* -i or --input_file: The path to the input file. This argument is required.
* -o or --output_file: The path to the output file. This argument is optional. If not provided, the default output file name will be used.

### Notes
The scripts use the fastavro library, which requires a schema for Avro conversion. Ensure that the schema provided in `schema.py` matches the structure of your JSON data.
Make sure the JSON data file is correctly formatted and contains valid JSON objects.
The execution time of the conversion process will be displayed at the end.

`avro_to_json_converter.py` works with the same instructions.