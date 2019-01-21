import sys

from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

class CustomSlider(QSlider):
    def __init__(self, *args):
        QSlider.__init__(self, *args)

    @pyqtSlot(int)
    @pyqtSlot(str) # decorator can make the function making input as int and str as function overloading
    def setValue(self, value):
        value = int(value)
        QSlider.setValue(self, value)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.cnt = 0
        self.le = QLineEdit()
        self.dial = QDial()
        self.sld = CustomSlider(Qt.Horizontal)

        self.init_widget()
