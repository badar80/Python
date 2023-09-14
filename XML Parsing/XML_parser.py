# Specify the path to your XML file
xml_file = 'path to your XML file'

import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    # Create an empty dictionary to store the extracted data
    data_dict = {}

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate through 'person' elements and extract data
    for person in root.findall('person'):
        name = person.find('name').text
        age = int(person.find('age').text)  # Convert age to an integer
        data_dict[name] = age

    return data_dict

# Parse the XML and store the data in a dictionary
result_dict = parse_xml(xml_file)

# Print the extracted data
for name, age in result_dict.items():
    print(f"Name: {name}, Age: {age}")
