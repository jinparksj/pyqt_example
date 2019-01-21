import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

class CustomSlider(QSlider):
    def __init__(self, *args, **kwargs):
        QSlider.__init__(self, *args)

    @pyqtSlot(int, name="setValue")
    def set_int_value(self, value):
        QSlider.setValue(self, value)

    @pyqtSlot(str, name="setValue")
    def set_str_value(self, value):
        try:
            value = int(value)
        except Exception:
            value = 0
        QSlider.setValue(self, value)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.le = QLineEdit()
        self.dial = QDial()
        self.sld = CustomSlider(Qt.Horizontal)

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("custom slot")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        control_lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
        self.setLayout(form_lbx)

        self.le.setMaximumWidth(40)

        #connect between signal and slot
        self.sld.valueChanged.connect(self.valueChanged)
        self.le.textChanged.connect(self.sld.setValue)
        self.dial.valueChanged.connect(self.sld.setValue)

        form_lbx.addWidget(self.dial)
        form_lbx.addLayout(control_lbx)
        control_lbx.addWidget(self.sld)
        control_lbx.addWidget(self.le)


    @pyqtSlot(int, name="valueChanged")
    def value_changed(self, value):
        self.le.setText(str(value))
        self.dial.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec())




