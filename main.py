"""
======================================
Rotate Dicom image and Create 3D array
======================================

"""

# author  : Lee, Junyoung
# license : SNU RPLab

import os
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np
import pydicom as dcm

print(__doc__)

PathXml = 'C:/INFINITT/BNCT_TEMP/'

whole_files = os.listdir(PathXml)
list(whole_files)
xml_file = os.path.join(PathXml, whole_files[0])
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

CT_image = root.find("CTImage")

CT_dir = []
CT_slide = []

for child in CT_image:
    CTD = CT_image.findtext(child.tag)
    CT_dir.append(CTD)
    CT_slide.append(dcm.dcmread(CTD))

ps = CT_slide[0].PixelSpacing
ss = CT_slide[0].SliceThickness
ax_aspect = ps[1] / ps[0]
sag_aspect = ps[1] / ss
cor_aspect = ss / ps[0]

img_shape = list(CT_slide[0].pixel_array.shape)
img_shape.append(len(CT_slide))
img3d = np.zeros(img_shape)

# fill 3d array with the images from the files

for i, s in enumerate(CT_slide):
    img2d = s.pixel_array
    img3d[:, :, i] = img2d

# plot 3 orthogonal slices
a1 = plt.subplot(2, 2, 1)
plt.imshow(img3d[:, :, img_shape[2] // 2])
a1.set_aspect(ax_aspect)

a2 = plt.subplot(2, 2, 2)
plt.imshow(img3d[:, img_shape[1] // 2, :])
a2.set_aspect(sag_aspect)

a3 = plt.subplot(2, 2, 3)
plt.imshow(img3d[img_shape[0] // 2, :, :].T)
a3.set_aspect(cor_aspect)

plt.show()

##################################################
