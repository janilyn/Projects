'''
TODO: missing functionalities in auto contouring:
1. change the values in the information section whenever a file is opened
2. code for the open button
3. add try function for cases wherein the user opens an invalid file
4. add a case wherein if the file opened is the same one, it will not do anything
5. open a msgbox that says (3)
6. file path will be shown in the textbox in the directory
7. add code for the thorax and abdomen 
8. add code for the generate and clear button
9. ranged slider for the vmin and vmax of the images
10. cmap option code
        gray
        jet
        viridis
        plasma
        hot
        coolwarm
        cool
        bone
'''
import os

import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from imageclass import img

from PyQt5.uic import loadUi
from qtrangeslider.qtcompat.QtCore import Qt

#test
from random import randint

nslice = [0,0,0]
graph_list = [None,None,None]

class Mainwind(QMainWindow):
    '''
    This is the code for the whole UI
    '''

    def __init__(self):
        '''
        Executes at the start of the run. Will determine how the program will work.\n
        Some important values were initialized here to avoid errors at the start of the run.
        '''
        QMainWindow.__init__(self)
        loadUi("maingui.ui",self)

        self.changeValue = [0,0,0]
        """self.ACsliderImg1.setOrientation(Qt.Horizontal)
        self.ACsliderImg1.setMaximum(0)
        self.ACsliderImg1.setEnabled(0)"""
        self.qtconnects()

    def change_file(self):
        randomnum = randint(0, 1)
        if randomnum == 0:
            self.imgfile = img(str(os.getcwd())+"/001_ph-mouse_40kV_DS10_masked.nrrd")
        else:
            self.imgfile = img(str(os.getcwd())+"/LungOAR_135_0000.nii.gz")
        self.update_info()
        self.update_graph(3)

    def update_info(self):
        strdim = ""
        for i in range(3):
            strdim += str(self.imgfile.dimension[i])
            if i != 2:
                strdim += ", "
        self.ACresultDim.setText(strdim)
        
        strspacing = ""
        for i in range(3):
            strspacing += str(round(self.imgfile.spacing[i],3))
            if i != 2:
                strspacing += " , "
        self.ACresultSpacing.setText(strspacing)

        strhurange = str(self.imgfile.HU_range[0]) + " , " + str(self.imgfile.HU_range[1])
        self.ACresultHUR.setText(strhurange)

    def update_graph(self, n : int):
        ''' 
        Changes the all images shown on the matplotlib graphs\n
        ------
        Parameters:\n
            1. self: the class itself
            2. n: determines what images the function will update
                    - (0) left image only , (1) middle image only, (2) right image only, (3) all images
        '''
        if n == 0:
            self.ACimg1.updateGraph(self.imgfile, 0, self.ACsliderImg1.value())
        elif n == 1:
            self.ACimg2.updateGraph(self.imgfile, 1, self.ACsliderImg2.value())
        elif n == 2:
            self.ACimg3.updateGraph(self.imgfile, 2, self.ACsliderImg3.value())
        elif n == 3:
            self.ACimg1.updateGraph(self.imgfile, 0, self.ACsliderImg1.value())
            self.ACimg2.updateGraph(self.imgfile, 1, self.ACsliderImg2.value())
            self.ACimg3.updateGraph(self.imgfile, 2, self.ACsliderImg3.value())

    def update_rangegraph(self):
        self.imgfile.vmin, self.imgfile.vmax = self.ACwidgetDoubleSlider.value()
        self.update_graph(3)

    def init_slice(self):
        '''
        Sets the maximum value of the three sliders based on the file opened. This is called everytime the open button is pressed\n
        ------
        Note:\n
            1. At the start of each program run, there is no file being viewed so the initialized max value of the sliders is 0. 
        '''
        self.ACsliderImg1.setMaximum(self.imgfile.dimension[0]-1)
        self.ACsliderImg2.setMaximum(self.imgfile.dimension[1]-1)
        self.ACsliderImg3.setMaximum(self.imgfile.dimension[2]-1)

    def update_slice_labels(self, n : int):
        '''
        Shows which slice is being viewed in the image by changing the value of its respective frame. The slice number will be determined by the slider value.\n
        ------
        Parameters: \n
            1. self: the class itself
            2. n: determines what frames the function will update
                    - (0) left frame only , (1) middle frame only, (2) right frame only, (3) all frames
        ------
        Note:\n
            1. Initially the starting and max values will both be 0 so the starting range will be 0 to 0.
            2. After a file is opened, the max value will be changed to the dimensions of the array while the starting value will remain 0 until the slider thumb is moved.
        '''
        if n == 0:
            self.ACgroupImage1.setTitle("Axial: " + str(self.imgfile.nslice[0]+1) + "/" + str(self.imgfile.dimension[0]))
        elif n == 1:
            self.ACgroupImage2.setTitle("Coronal: " + str(self.imgfile.nslice[1]+1) + "/" + str(self.imgfile.dimension[1]))
        elif n == 2:
            self.ACgroupImage3.setTitle("Sagittal: " + str(self.imgfile.nslice[2]+1) + "/" + str(self.imgfile.dimension[2]))
        elif n == 3:
            self.ACgroupImage1.setTitle("Axial: " + str(self.imgfile.nslice[0]+1) + "/" + str(self.imgfile.dimension[0]))
            self.ACgroupImage2.setTitle("Coronal: " + str(self.imgfile.nslice[1]+1) + "/" + str(self.imgfile.dimension[1]))
            self.ACgroupImage3.setTitle("Sagittal: " + str(self.imgfile.nslice[2]+1) + "/" + str(self.imgfile.dimension[2]))

    def qtconnects(self):
        self.connect_OpenButton()
        self.connect_Slider_To_Graph()
        self.connect_Slider_to_Frame()
        self.connect_RangedSlider_to_Graph()
        
    def connect_OpenButton(self):
        '''
        Connects open button to the image, sliders, and frame labels.\n
        ------
        Parameters:\n
            1. the class itself
        ------
        Note:\n
            1. The image widget and frame labels change every time open button is clicked.
            2. The max value of the slider will also change depending on the dimensions of the images
        '''
        self.ACpushOpen.clicked.connect(self.change_file)
        self.ACpushOpen.clicked.connect(self.init_slice)
        self.ACpushOpen.clicked.connect(lambda: self.update_slice_labels(3))
        self.ACpushOpen.clicked.connect(lambda: self.ACwidgetDoubleSlider.update_rangeslider(self.imgfile))
    
    def connect_RangedSlider_to_Graph(self):
        self.ACwidgetDoubleSlider.slider.valueChanged.connect(self.update_rangegraph)

    def connect_Slider_To_Graph(self):
        '''
        Connects sliders to its respective image widget\n
        ------
        Parameters\n
        1. self: the class itself\n
        ------
        Note:\n
            1. The slider value will be the slice number of the image widget.
            2. The slice number will determine the image to be displayed in the UI.
            3. The image is updated everytime the slider thumb is moved.
        '''
        self.ACsliderImg1.valueChanged.connect(lambda: self.update_graph(0))
        self.ACsliderImg2.valueChanged.connect(lambda: self.update_graph(1))
        self.ACsliderImg3.valueChanged.connect(lambda: self.update_graph(2))

    def connect_Slider_to_Frame(self):
        '''
        Connects the sliders to the its respective frame.\n
        ------
        Note:\n
            1. The slider value (slice number) will be displayed in the frame title.
            2. This will be 
        '''
        self.ACsliderImg1.valueChanged.connect(lambda: self.update_slice_labels(0))
        self.ACsliderImg2.valueChanged.connect(lambda: self.update_slice_labels(1))
        self.ACsliderImg3.valueChanged.connect(lambda: self.update_slice_labels(2))

if __name__ == '__main__':
    app = QApplication([])
    window = Mainwind()
    window.show()
    app.exec_()
