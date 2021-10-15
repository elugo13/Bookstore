from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.Ui_main_window import Ui_MainWindow
from ui.Ui_dialog_add_book import Ui_dialog_add_book
from ui.Ui_dialog_delete_book import Ui_dialog_delete
from ui.Ui_dialog_edit_book import Ui_dialog_edit_book
from modules.books_manager import BooksManager
from os import path
from typing import List
from modules.book import Book


class DialogAdd(QDialog):

    def __init__(self, parent=None) -> None:
        super(DialogAdd, self).__init__(parent)
        self.ui = Ui_dialog_add_book()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class DialogEdit(QDialog):

    def __init__(self, parent=None) -> None:
        super(DialogEdit, self).__init__(parent)
        self.ui = Ui_dialog_edit_book()
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
        # issued_books = self.get_books_by_status(is_issued=True)
        # unissued_books = self.get_books_by_status(is_issued=False)
        # all_books = self.books_manager.load_books()

        # self.load_data_table(self.tbl_issued_books, issued_books)
        # self.load_data_table(self.tbl_unissued_books, unissued_books)
        # self.load_data_table(self.tbl_all_books, all_books)
        self.fill_tables()

        self.action_exit.triggered.connect(self.exit_app)
        self.btn_new_book.clicked.connect(self.show_dialog_add_book)
        self.btn_edit_issued.clicked.connect(lambda: self.edit_book(self.tbl_issued_books))
        self.btn_edit_unissued.clicked.connect(lambda: self.edit_book(self.tbl_unissued_books))

    def fill_tables(self) -> None:
        issued_books = self.get_books_by_status(is_issued=True)
        unissued_books = self.get_books_by_status(is_issued=False)
        all_books = self.books_manager.load_books()

        self.load_data_table(self.tbl_issued_books, issued_books)
        self.load_data_table(self.tbl_unissued_books, unissued_books)
        self.load_data_table(self.tbl_all_books, all_books)

    def exit_app(self) -> None:
        exit()

    def load_books(self) -> List[Book]:
        return self.books_manager.load_books()

    def get_books_by_status(self, is_issued=True) \
            -> List[Book]:
        if is_issued:
            return self.books_manager.get_issued_books()
        else:
            return self.books_manager.get_unissued_books()

    def load_data_table(self, table: QTableWidget, books: List[Book]):
        table.setRowCount(len(books))
        for index, book in enumerate(books):
            book = book.to_dict()
            for book_index, attr in enumerate(book):
                table.setItem(index, book_index,
                              QTableWidgetItem(str(book[attr])))
                table.item(index, book_index).setFlags(
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def show_dialog_add_book(self) -> None:
        input_dialog = DialogAdd()
        input_dialog.ui.buttonBox.accepted.connect(
            lambda: self.save_new_book(input_dialog.ui))
        input_dialog.ui.spin_id.setEnabled(False)
        next_book_id = self.books_manager.get_last_book_id() + 1
        input_dialog.ui.spin_id.setValue(next_book_id)
        input_dialog.exec()

    def edit_book(self, table: QTableWidget) -> None:
        selected_row = table.currentRow()
        if selected_row >= 0:
            book_id = int(table.item(selected_row, 0).text())
            book = self.books_manager.find_book(book_id)
            dlg_edit = DialogEdit()
            dlg_edit.ui.buttonBox.accepted.connect(
                lambda: self.save_existing_book(dlg_edit.ui))

            dlg_edit.ui.spin_id.setValue(book.id)
            dlg_edit.ui.txt_name.setText(book.name)
            dlg_edit.ui.txt_description.setText(book.description)
            dlg_edit.ui.txt_isbn.setText(book.isbn)
            dlg_edit.ui.spin_page_count.setValue(book.page_count)
            if book.issued:
                dlg_edit.ui.rad_yes.setChecked(True)
            else:
                dlg_edit.ui.rad_no.setChecked(True)
            dlg_edit.ui.txt_author.setText(book.author)
            dlg_edit.ui.spin_year.setValue(book.year)
            dlg_edit.exec()
    
    def save_existing_book(self, ui: Ui_dialog_edit_book) -> None:
        book_info = {
            "id": int(ui.spin_id.text()),
            "name": ui.txt_name.text(),
            "description": ui.txt_description.text(),
            "isbn": ui.txt_isbn.text(),
            "page_count": int(ui.spin_page_count.text()),
            "issued": ui.rad_yes.isChecked(),
            "author": ui.txt_author.text(),
            "year": int(ui.spin_year.text())
        }

        is_valid_book = self.validate_book(book_info)
        if not is_valid_book:
            return
        
        self.books_manager.update_book(book_info)
        self.fill_tables()

    def save_new_book(self, ui: Ui_dialog_add_book) -> None:
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

        self.books_manager.add_new_book(new_book)

    def validate_book(self, book: dict) -> bool:
        for attr in book:
            if attr != 'issued' and not book[attr]:
                return False
        return True


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
