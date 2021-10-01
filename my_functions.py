from book import Book
import json
from typing import List


def print_options() -> None:
    print("Press the specific button for that action")
    print("1. Create a new book")
    print("2. Save books locally")
    print("3. Load books from the disk")
    print("4. Issue book")
    print("5. Return a book")
    print("6. Update a book")
    print("7. Show all books")
    print("8. Show book")

def create_book() -> Book:
    print("Please enter your book information")
    book_input = input_book_info()
    book = Book(
        book_input['id'],
        book_input['name'],
        book_input['description'],
        book_input['isbn'],
        book_input['page_count'],
        book_input['issued'],
        book_input['author'],
        book_input['year']
    )
    return book

def input_book_info() -> dict:
    id = input("ID: ")
    name = input("Name: ")
    description = input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page count: "))
    issued = input("Issued y/Y for True, anything else for False: ").upper()
    issued = issued == 'Y'
    author = input("Author name: ")
    year = int(input("Year: "))
    return {
            "id": id,
            "name": name,
            "description": description,
            "isbn": isbn,
            "page_count": page_count,
            "issued": issued,
            "author": author,
            "year": year
        }

def save_books(books: List[Book]) -> None:
    json_books = [book.to_dict() for book in books]
    try:
        with open("books.dat", "w") as books_file:
            books_file.write(json.dumps(json_books, indent=4))
    except:
        print("We had an error saving books")
