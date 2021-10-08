from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)

        self.action_exit.triggered.connect(self.exit_app)


    def exit_app(self) -> None:
        exit()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()