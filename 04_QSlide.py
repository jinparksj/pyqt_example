import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.lb = QLabel()
        self.sd = QSlider(Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        self.sd.valueChanged.connect(lambda v: self.lb.setText(str(v)))
        form_lbx.addWidget(self.sd)
        form_lbx.addWidget(self.lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())