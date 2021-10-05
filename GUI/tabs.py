from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Lists")
        self.resize(1280, 720)

        layout = QVBoxLayout()

        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.addTab(QLabel("THIS IS TAB 1\n1\n1"), "TAB one")
        tabs.addTab(QLabel("THIS IS TAB 2\n222\n2"), "TAB two")
        tabs.addTab(QLabel("THIS IS TAB 3tres\n3tres\n3tres"), "TAB Three")

        layout.addWidget(tabs)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self, item):
        print(item.text())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()