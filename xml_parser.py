import numpy as np
import pydicom as dcm

def tumor_ROINo(root):
    ROI = root.find('ROI')
    tumor_ROI = []
    for child in ROI:
        ITEM = ROI.find(child.tag)
        ROI_type = ITEM.findtext('ROIType')
        if ROI_type == 'tumor':
            tumor_ROI.append(int(ITEM.findtext('ROINo')))

    return tumor_ROI


def image_3d(root):
    CT_image = root.find("CTImage")

    CT_dir = []
    CT_slide = []

    for child in CT_image:
        CTD = CT_image.findtext(child.tag)
        CT_dir.append(CTD)
        CT_slide.append(dcm.dcmread(CTD))

    img_shape = list(CT_slide[0].pixel_array.shape)
    img_shape.append(len(CT_slide))
    img3d = np.zeros(img_shape)

    # fill 3d array with the images from the files

    for i, s in enumerate(CT_slide):
        img2d = s.pixel_array
        img3d[:, :, i] = img2d

    return img3d


def data_spacing(root):
    CT_image = root.find("CTImage")

    CT_dir = []
    CT_slide = []

    for child in CT_image:
        CTD = CT_image.findtext(child.tag)
        CT_dir.append(CTD)
        CT_slide.append(dcm.dcmread(CTD))

    ps = CT_slide[0].PixelSpacing
    ss = CT_slide[0].SliceThickness
    ps.append(ss)

    return ps
