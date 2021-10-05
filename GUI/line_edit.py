from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Line edit (input field)")
        self.resize(1280, 720)

        layout = QVBoxLayout()
        input_field = QLineEdit()

        layout.addWidget(input_field)

        input_field.returnPressed.connect(lambda: print(input_field.text()))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()