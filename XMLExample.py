import xml.etree.ElementTree as ET
import dateutil.parser

xml_file = ET.parse('sales-data.xml')
rt = xml_file.getroot()
for person in rt.findall('person'):
    id = person.find('id')

val = int('1')
some_string = str(123)
flt = float('1.23')
ts = dateutil.parser.parse('2021-09-21')
