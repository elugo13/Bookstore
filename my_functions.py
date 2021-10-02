from book import Book
import json
from typing import List


def print_options() -> None:
    print("Book Store\n")
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

def load_books():
    try:
        with open("books.dat", 'r') as open_file:
            loaded_books = json.loads(open_file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(
                book['id'],
                book['name'],
                book['description'],
                book['isbn'],
                book['page_count'],
                book['issued'],
                book['author'],
                book['year']
            )
            books.append(new_obj)
        print(f"Books loaded: {len(books)}")
        return books
    except:
        print("The file doesn't  exist or an error ocurred during loading")

def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None

def issue_book(books):
    id = input("Enter the id of the book you want to issue: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued")
    else:
        print("Could not find the book you are looking for")

def return_book(books):
    id = input("Enter the id of the book you want to return: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find the book you are looking for")

def update_book(books):
    id = input("Enter the id of the book you want to update: ")
    index = find_book(books, id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated")
    else:
        print("We could not find your book")

def show_all_books(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Please enter the id of the book you're looking for: ")
    index = find_book(books, id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("We could not find the book you are looking for")