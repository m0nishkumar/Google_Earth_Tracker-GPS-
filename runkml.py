from pykml import parser
with open('test3.kml', 'r') as kml_file:
    root = parser.parse(kml_file).getroot()
for i in root.findall('{http://www.opengis.net/kml/2.2}Document/{http://www.opengis.net/kml/2.2}Placemark/{http://www.opengis.net/kml/2.2}Point'):
    print(i.coordinates)