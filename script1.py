import csv
import random
import string
import xml.etree.ElementTree as ET

def generate_random_hex(length):
    """Generate a random hex ID of given length."""
    hex_chars = string.hexdigits[:-6]  # Exclude lowercase letters from hex digits
    return ''.join(random.choice(hex_chars) for _ in range(length))

def csv_to_xml(csv_file, xml_file):
    """Convert CSV file to XML and add random hex ID."""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    root = ET.Element('data')
    for entry in data:

        entry_element = ET.SubElement(root, 'entry')
        for key, value in entry.items():
            field_element = ET.SubElement(entry_element, key)
            field_element.text = value
            #hex_id = generate_random_hex(8)
            #entry['hex_id'] = hex_id


    tree = ET.ElementTree(root)
    tree.write(xml_file)

# Usage example
def main():
    fileName = input("enter csv file name: ")
    csv_file = fileName + ".csv"
    xml_file = fileName + ".xml"
    csv_to_xml(csv_file, xml_file)

if __name__ == '__main__':
    main()