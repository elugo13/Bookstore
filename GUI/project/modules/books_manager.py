import json
from modules.book import Book
from typing import List
from os import path

class BooksManager:

    BOOKS_DB_FILE_NAME = 'books.dat'

    def __init__(self, books_db_dir_path: str):
        self.db_dir_path = books_db_dir_path
        
    def load_books(self) -> List[Book]:
        books_file_path = path.join(self.db_dir_path, self.BOOKS_DB_FILE_NAME)
        try:
            books = []
            with open(books_file_path, mode='r') as f:
                books_info_dict = json.loads(f.read())
            for book_info in books_info_dict:
                book_obj = Book(book_info=book_info)
                books.append(book_obj)
            return books
        except IOError:
            return []

    def get_issued_books(self):
        books = self.load_books()
        issued_books = list(filter(lambda book: book.issued == True, books))
        return issued_books

    def get_unissued_books(self):
        books = self.load_books()
        issued_books = list(filter(lambda book: book.issued == False, books))
        return issued_books
    
    def find_book(self, book_id: int) -> Book:
        books = self.load_books()
        for book in books:
            if book.id == book_id:
                return book
        return None

    def add_new_book(self, book_info: dict) -> None:
        books = self.load_books()
        new_book = Book(book_info=book_info)
        books.append(new_book)
        self.save_books(books)
        return books

    def save_books(self, books: List[Book]) -> None:
        books_file_path = path.join(self.db_dir_path, self.BOOKS_DB_FILE_NAME)
        json_books = []
        for book in books:
            json_books.append(book.to_dict())
        
        with open(books_file_path, mode='w') as f:
            f.write(json.dumps(json_books, indent=4))

    def update_book(self, book_info: dict) -> None:
        books = self.load_books()
        book = Book(book_info)
        books = list(filter(lambda bk: bk.id != book.id, books))
        books.append(book)
        self.save_books(books)
    
    def get_last_book_id(self) -> int:
        books = self.load_books()
        book_ids = []

        if len(books) == 0:
            return 0

        for book in books:
            book_ids.append(int(book.id))
        return max(book_ids)