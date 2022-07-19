import SimpleITK as sitk
import matplotlib.pylab as plt
import numpy as np
import pydicom as dicom
import pylidc as pl

pid = 'LIDC-IDRI-0001'
scan = pl.query(pl.Scan).filter(pl.Scan.patient_id == pid).first()
print(len(scan.annotations))
nods = scan.cluster_annotations()
scan.visualize(annotation_groups=nods)
