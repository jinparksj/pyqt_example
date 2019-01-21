import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.dl = QDial()
        self.sd = QSlider(Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        self.dl.valueChanged.connect(self.sd.setValue)
        self.sd.valueChanged.connect(self.dl.setValue)

        form_lbx.addWidget(self.dl)
        form_lbx.addWidget(self.sd)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec())