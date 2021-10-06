from posixpath import abspath
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Toolbars")
        self.resize(1280, 720)

        current_dir = path.dirname(path.abspath(__file__))
        icon_path = path.join(current_dir, "toolbar_icon_python_logo.png")

        layout = QVBoxLayout()

        toolbar = QToolBar("My toolbar")
        toolbar.setIconSize(QSize(16,16))
        icon1 = QIcon(icon_path)
        action_btn1 = QAction(icon1, "Paint", self)
        action_btn1.setCheckable(True)
        toolbar.addAction(action_btn1)
        toolbar.addSeparator()

        self.addToolBar(toolbar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self, item):
        print(item.text())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()