import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

import time


class TicGenerator(QThread):
    """
    5초마다 틱 신호를 전달
    """
    # 사용자 정의를 시그널 선언

    tic = pyqtSignal(name = "Tic")

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            t = int(time.time())
            if not t % 5 == 0:
                self.usleep(1)
                continue
            self.tic.emit()
            self.msleep(1000)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags = Qt.Widget)
        self.te = QTextEdit()
        self.tic_gen = TicGenerator()
        self.init_widget()
        self.tic_gen.start()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent = self)
        self.setLayout(form_lbx)

        self.tic_gen.tic.connect(lambda : self.te.insertPlainText(time.strftime("[%H : %M : %S] Tic! \n")))

        form_lbx.addWidget(self.te)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec())