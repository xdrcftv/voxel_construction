import os
import xml.etree.ElementTree as EleTree

import pydicom as dcm

import xml_parser

file_directory = 'C:/INFINITT/BNCT_TEMP'

whole_files = os.listdir(file_directory)
list(whole_files)
xml_file = os.path.join(file_directory, whole_files[0])
xml_doc = EleTree.parse(xml_file)

root = xml_doc.getroot()

struct_dir = root.findtext('RTStructure')
RT_struct = dcm.dcmread(struct_dir)
print(type(RT_struct))
ROI_contour = RT_struct.ROIContourSequence

tumor_ROI = xml_parser.tumor_ROINo(root)

tumor1 = ROI_contour[3]

print(list(tumor1._dict.items()))
print(tumor1[(0x3006, 0x0040)])
#print(tumor1.ContourSequence[0].ContourData)

#for i in range(len(tumor1.ContourSequence)):
#                UID = tumor1.ContourSequence[i].ContourImageSequence[0].ReferencedSOPInstanceUID
#                reference_list = np.append(reference_list, UID)
# for i in tumor_ROI:
#     print(ROI_contour[i-1])

