from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(MyDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("My dialog box")
        self.resize(350, 250)
        self.label = QLabel("COOL!")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)




class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Dialog box")
        self.resize(1280, 720)

        layout = QVBoxLayout()

        btn = QPushButton("press me")
        btn.pressed.connect(self.dialog_handler)

        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def dialog_handler(self):
        dialog = MyDialog()
        dialog.label.setText("MUCH MORE COOLER!")
        dialog.exec()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()