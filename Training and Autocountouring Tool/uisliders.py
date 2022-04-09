from typing import Tuple

from PyQt5.QtWidgets import *
from qtrangeslider.qtcompat.QtCore import Qt
from qtrangeslider import QLabeledRangeSlider, QDoubleSlider

from imageclass import img

class sliderColorMap(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.slider = QLabeledRangeSlider()
        self.defaultStyle()

        self.displaywidget()
    
    def update_rangeslider(self, image : img):
        self.setEnabled(True)
        self.setRange(image.HU_range[0], image.HU_range[1])
        self.setValue((image.HU_range[0], image.HU_range[1]))

    def setRange(self, min : int, max : int):
        self.slider.setRange(min,max)

    def setEnabled(self, nbool : bool):
        self.slider.setEnabled(nbool)     

    def setOrientation(self, orientation : Qt.Orientation):
        self.slider.setOrientation(orientation)

    def setMaximum(self, max : int):
        self.slider.setMaximum(max)

    def setMinimum(self, min : int):
        self.slider.setMinimum(min)
    
    def value(self):
        return self.slider.value()

    def setValue(self, n : Tuple[int,int]):
        return self.slider.setValue(n)

    def defaultStyle(self):
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(1)
        self.setValue((0,1))
        self.slider.setRange(0,1)
        self.setEnabled(False)

    def displaywidget(self):
        slider_layout = QVBoxLayout()
        slider_layout.setSpacing(0)
        slider_layout.setContentsMargins(0,0,0,0)
        slider_layout.addWidget(self.slider)
        self.setLayout(slider_layout)

class sliderGraph(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.slider = QLabeledRangeSlider()
        self.defaultStyle()

        self.displaywidget()
    
    def update_slider(self, image : img, n :int):
        self.setEnabled(True)
        self.setRange(image.HU_range[0], image.HU_range[1])

    def setRange(self, min : int, max : int):
        self.slider.setRange(min,max)

    def setEnabled(self, nbool : bool):
        self.slider.setEnabled(nbool)     

    def setOrientation(self, orientation : Qt.Orientation):
        self.slider.setOrientation(orientation)

    def setMaximum(self, max : int):
        self.slider.setMaximum(max)

    def setMinimum(self, min : int):
        self.slider.setMinimum(min)
    
    def value(self):
        return self.slider.value()

    def setValue(self, n : Tuple[int,int]):
        return self.slider.setValue(n)

    def defaultStyle(self):
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(1)
        self.setValue((0,1))
        self.slider.setRange(0,1)
        self.setEnabled(False)

    def displaywidget(self):
        slider_layout = QVBoxLayout()
        slider_layout.setSpacing(0)
        slider_layout.setContentsMargins(0,0,0,0)
        slider_layout.addWidget(self.slider)
        self.setLayout(slider_layout)
