from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.project.modules.my_functions import BOOKS_DB_FILE_NAME
from ui.Ui_main_window import Ui_MainWindow
from ui.Ui_dialog_add_book import Ui_dialog_add_book
from ui.Ui_dialog_delete_book import Ui_dialog_delete
from ui.Ui_dialog_edit_book import Ui_dialog_edit_book
from modules.books_manager import BooksManager
from os import path


class DialogAdd(QDialog):

    def __init__(self, parent=None) -> None:
        super(DialogAdd, self).__init__(parent)
        self.ui = Ui_dialog_add_book()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        current_path = path.dirname(path.abspath(__file__))
        books_db_dir_path = path.join(current_path, 'db')

        self.books_manager = BooksManager(books_db_dir_path)
        
        self.books = self.books_manager.load_books()

        self.action_exit.triggered.connect(self.exit_app)
        self.btn_new_book.clicked.connect(self.show_dialog_add_book)

    def exit_app(self) -> None:
        exit()

    def show_dialog_add_book(self) -> None:
        input_dialog = DialogAdd()
        input_dialog.ui.buttonBox.accepted.connect(lambda: self.save_new_book(input_dialog.ui))
        input_dialog.ui.spin_id.setEnabled(False)
        next_book_id = self.books_manager.get_last_id(self.books) + 1
        input_dialog.ui.spin_id.setValue(next_book_id)
        input_dialog.exec()
    
    def save_new_book(self, ui):
        new_book = {
            "id": int(ui.spin_id.text()),
            "name": ui.txt_name.text(),
            "description": ui.txt_description.text(),
            "isbn": ui.txt_isbn.text(),
            "page_count": int(ui.spin_page_count.text()),
            "issued": ui.rad_yes.isChecked(),
            "author": ui.txt_author.text(),
            "year": int(ui.spin_year.text())
        }

        is_valid_book = self.validate_book(new_book)
        if not is_valid_book:
            return
        
        self.books = self.books_manager.add_new_book(self.books, new_book)
        self.books_manager.save_books(self.books)
        self.books = self.books_manager.load_books()

    def validate_book(self, book: dict) -> bool:
        for attr in book:
            if attr != 'issued' and not book[attr]:
                return False
        return True


app = QApplication([])
window = MainWindow()
window.show()
app.exec()