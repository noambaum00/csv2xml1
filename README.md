# scv2xml1
This is a Python script that converts a CSV file to XML format and adds a random hex ID to each entry.

## Requirements

- Python 3.x

## Usage

1. Make sure you have a CSV file with data that you want to convert to XML. The CSV file should be placed in the same directory as the script.

2. enter the CSV file name 

3. Run the script `script1.py` using Python:

   ```shell
   python script1.py
The script will read the csv file, convert it to XML, and generate a file named data.xml in the same directory.

Open the generated xml file to view the converted data with added random hex IDs.

Customization
If you want to change the length of the random hex ID, you can modify the generate_random_hex function in the script. Currently, it generates an 8-character hex ID.
License
This project is licensed under the GNU General Public License v3.0.

Feel free to customize and use it according to your needs.

Acknowledgements
The script uses the Python standard libraries csv and xml.etree.ElementTree for CSV parsing and XML generation, respectively.