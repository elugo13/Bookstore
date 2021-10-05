from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Combo boxes")
        self.resize(1280, 720)

        combo = QComboBox()
        combo.addItems(['Easy', 'Hard', 'Medium'])

        btn = QPushButton("Start")
        btn.pressed.connect(lambda: self.show_selected(combo))
        
        layout = QVBoxLayout()

        layout.addWidget(combo)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_selected(self, combo) -> None:
        print(combo.currentText())

app = QApplication([])
window = MainWindow()
window.show()
app.exec()