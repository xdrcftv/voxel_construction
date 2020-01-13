import os
import xml.etree.ElementTree as ET

import xml_parser

file_directory = 'C:/INFINITT/BNCT_TEMP/'

whole_files = os.listdir(file_directory)
list(whole_files)
xml_file = os.path.join(file_directory, whole_files[0])
xml_doc = ET.parse(xml_file)

root = xml_doc.getroot()

##########################################################################

Beam = root.find("Beam")

Source_Point = []
for child in Beam.iter("SourcePoint"):
    Src_Coordinate = list(child.text.split('\\'))
    Source_Point.append(Src_Coordinate)

Reference_Point = []
for child in Beam.iter("ReferencePoint"):
    Ref_Coordinate = list(child.text.split('\\'))
    Reference_Point.append(Ref_Coordinate)

print(Source_Point[0])
print(Reference_Point[0])

# beam_orientation = np.subtract(Reference_Point[0], Source_Point[0])

# print(beam_orientation)

##########################################################################

img3d = xml_parser.image_3d(root)
spacing = xml_parser.data_spacing(root)

ax_aspect = spacing[1] / spacing[0]
sag_aspect = spacing[1] / spacing[2]
cor_aspect = spacing[2] / spacing[0]


##################################################
