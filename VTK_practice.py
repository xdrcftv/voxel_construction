import os
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np
import pydicom as dcm
import scipy.ndimage.interpolation as ndinter

PathXml = 'C:/INFINITT/BNCT_TEMP/'

whole_files = os.listdir(PathXml)
list(whole_files)
xml_file = os.path.join(PathXml, whole_files[0])
xml_doc = ET.parse(xml_file)

root = xml_doc.getroot()

CT_image = root.find("CTImage")

CT_dir = []
CT_slide = []

for child in CT_image:
    CTD = CT_image.findtext(child.tag)
    CT_dir.append(CTD)
    CT_slide.append(dcm.dcmread(CTD))

Ref_CT = CT_slide[0]
#Load dimensions [columns, rows, slices]
ConstPixelDims = (int(Ref_CT.Columns), int(Ref_CT.Rows), len(CT_slide))

#Load spacing values (in mm)
ConstPixelSpacing = (float(Ref_CT.PixelSpacing[1]), float(Ref_CT.PixelSpacing[0]), float(Ref_CT.SliceThickness))

x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
y = np.arange(-(ConstPixelDims[1]+1)*ConstPixelSpacing[1], 0.0, ConstPixelSpacing[1])
z = np.arange(0.0, (ConstPixelDims[2]+1)*ConstPixelSpacing[2], ConstPixelSpacing[2])

ArrayDicom = np.zeros(ConstPixelDims, dtype=Ref_CT.pixel_array.dtype)

for i, DCMfile in enumerate(CT_slide):
    ArrayDicom[:, :, i] = DCMfile.pixel_array
"""
 plt.figure(dpi=300)
 plt.axes().set_aspect('equal', 'datalim')
 plt.set_cmap(plt.gray())
 plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, 50]))
 plt.show()
"""
ResArray = ndinter.zoom(ArrayDicom, ConstPixelSpacing, order=1)
plt.figure(dpi=300)
plt.axes().set_aspect('equal', 'datalim')
plt.set_cmap(plt.gray())
#plt.pcolormesh(x, y, ResArray[:, :, 150]))
plt.imshow(ResArray[:, :, 100])

plt.show()