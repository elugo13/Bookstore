import json
from modules.book import Book
from typing import List
from os import path


BOOKS_DB_FILE_NAME = 'books.dat'

def load_books(db_dir_path) -> List[Book]:
    books_file_path = path.join(db_dir_path, BOOKS_DB_FILE_NAME)
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

def add_new_book(book_info: dict):
    books = load_books()
    new_book = Book(book_info=book_info)
    new_book = assign_valid_id(books, new_book)
    books.append(new_book)
    save_books(books)

def save_books(books: List[Book], db_dir_path) -> None:
    books_file_path = path.join(db_dir_path, BOOKS_DB_FILE_NAME)
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    
    with open(books_file_path, mode='w') as f:
        f.write(json.dumps(json_books, indent=4))

def assign_valid_id(books: List[Book], new_book: Book) -> List[Book]:
    book_ids = []
    for book in books:
        book_ids.append(int(book.id))
    if not new_book.id in book_ids:
        return new_book
    else:
        new_book.id = max(book_ids) + 1
        return new_book