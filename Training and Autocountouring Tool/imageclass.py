import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np

class img:
    def __init__(self, path):
        self.nslice = [0,0,0]
        self.image = sitk.ReadImage(path)
        self.spacing = self.image.GetSpacing()

        self.array = sitk.GetArrayFromImage(self.image)
        self.dimension = self.array.shape
        self.HU_range = [np.min(self.array), np.max(self.array)]
        self.vmin, self.vmax = self.HU_range
    
    def getslices(self, n, nslice):
        self.n = n
        self.nslice[n] = nslice

    def array_slicer(self,):
        if self.n == 0:
            self.slice = self.array[self.nslice[self.n], :, :]
        elif self.n == 1:
            self.slice = self.array[:, self.nslice[self.n], :]
        elif self.n == 2:
            self.slice = self.array[:, :, self.nslice[self.n]]
    