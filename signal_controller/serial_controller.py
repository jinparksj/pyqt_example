import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtSerialPort import QSerialPortInfo

class SerialReadThread(QThread):
    """
    Should use QThread, because data always are transferred after connecting serial communication
    """
    #Custom Signal
    #transfer QByteArray type for communicating received data with same type

    def __init__(self, serial):
        QThread.__init__(self)
        self.cond = QWaitCondition()
        self._status = False
        self.mutex = QMutex()
        self.serial = serial

    def __del__(self):
        self.wait()

    def run(self):
        """
        if there is input data, generate signal
        :return:
        """

        while True:
            self.mutex.lock()
            if not self._status():
                self.cond.wait(self.mutex)

            buf = self.serial.readAll()
            if buf:
                self.received_data.emit(buf)
            self.usleep(1)
            self.mutex.unlock()

    def toggle_status(self):
        self._status = not self._status
        if self._status:
            self.cond.wakeAll()

    @pyqtSlot(bool, name = 'setStatus')
    def set_status(self, status):
        self._status = status
        if self._status:
            self.cond.wakeAll()


class SerialController(QWidget):
    # Serial Port Value
    BAUDRATES = (
        QSerialPort.Baud1200,
        QSerialPort.Baud2400,
        QSerialPort.Baud4800,
        QSerialPort.Baud9600,
        QSerialPort.Baud19200,
        QSerialPort.Baud38400,
        QSerialPort.Baud57600,
        QSerialPort.Baud115200
    )

    DATABITS = (
        QSerialPort.Data5,
        QSerialPort.Data6,
        QSerialPort.Data7,
        QSerialPort.Data8
    )

    PARITY = (
        QSerialPort.NoParity,
        QSerialPort.EvenParity,
        QSerialPort.OddParity,
        QSerialPort.SpaceParity,
        QSerialPort.MarkParity
    )

    STOPBITS = (
        QSerialPort.OneStop,
        QSerialPort.OneAndHalfStop,
        QSerialPort.TwoStop
    )

    received_data = pyqtSignal(QByteArray, name = "receivedData")
    sent_data = pyqtSignal(QByteArray, name = "sentData")

    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.gb = QGroupBox(self.tr("Serial"))
        self.cb_port = QComboBox()
        self.cb_baud_rate = QComboBox()
        self.cb_data_bits = QComboBox()
        self.cb_flow_control = QComboBox()
        self.cb_parity = QComboBox()
        self.cb_stop_bits = QComboBox()

        #serial instance
        #serial thread set up and start
        self.serial = QSerialPort()
        self.serial_info = QSerialPortInfo()
        self.serial_read_thread = SerialReadThread(self.serial)
        self.serial_read_thread.received_data.connect(lambda v: self.received_data.emit(v))
        self.serial_read_thread.start()

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Serial Controller")
        layout = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        grid_box = QGridLayout()

        grid_box.addWidget()





