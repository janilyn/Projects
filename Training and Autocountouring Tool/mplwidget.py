# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------

from turtle import update
import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
import matplotlib.cm as cm


from imageclass import img

class MplWidget(QWidget):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        self.dimension = [0,0,0]
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.figure.add_subplot(111)
        self.canvas.axes.axis('off')
        self.setLayout(vertical_layout)

        cid = self.figure.canvas.mpl_connect('button_press_event', self.onclick)

    #sets pixels transparent FIXME: https://stackoverflow.com/questions/17170229/setting-transparency-based-on-pixel-values-in-matplotlib 
    #FIXME: tweak updategraph function to make mask permanent through out the duration of the graph's image
    #FIXME: only assign the value 1 to the area selected by the user
    def onclick(self,event):
        masked_data = np.zeros((280,326))
        my_cmap = cm.gray
        my_cmap.set_under('k', alpha=0)

        for i in range(1,150):
            for j in range(4,60):
                masked_data[i,j] = 1
        
        self.ax.imshow(self.imageslice, cmap=self.cmap, vmin=self.vmin, vmax=self.vmax)
        self.ax.imshow(masked_data, cmap=my_cmap, interpolation='none', clim=[0.9, 1])

        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
        self.canvas.draw()

    def updateGraph(self, image : img, orientation : int, slice : int, parent = None):
        self.figure.clear()
        self.figure.patch.set_visible(False)

        self.ax = self.figure.add_subplot(111)
        
        self.figure.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        self.figure.patch.set_facecolor('whitesmoke')
        
        image.getslices(orientation,slice)
        image.array_slicer()

        self.imageslice = image.slice
        self.vmin = image.vmin
        self.vmax = image.vmax

        self.cmap = cm.jet
        self.dim = image.dimension[orientation]
        self.ax.imshow(image.slice, cmap=self.cmap, vmin=image.vmin, vmax=image.vmax)
        self.ax.axis('off')
        self.ax.axis('tight')
        self.ax.axis("image") 
        self.canvas.draw()


    

    