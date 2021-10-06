from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Layouts - Grid")
        self.resize(1280, 720)

        grid = QGridLayout()

        grid.addWidget(QLabel("Stuff 1"), 0, 0)
        grid.addWidget(QLabel("Stuff 2"), 1, 1)
        grid.addWidget(QLabel("Stuff 3"), 2, 2)
        grid.addWidget(QLabel("Stuff 4"), 3, 3)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def show_selected(self, item):
        print(item.text())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()