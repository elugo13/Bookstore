import my_functions as func
from os import path, system


func.print_options()
option = input()
books = []
current_dir = path.dirname(path.abspath(__file__))
books_file_path = path.join(current_dir, 'books.dat')

while option.upper() != 'X':
    if option == '1':
        book = func.create_book()
        books.append(book)
    elif option == '2':
        func.save_books(books, books_file_path)
    elif option == '3':
        books = func.load_books(books_file_path)
    elif option == '4':
        func.issue_book(books)
    elif option == '5':
        func.return_book(books)
    elif option == '6':
        func.update_book(books)
    elif option == '7':
        func.show_all_books(books)
    elif option == '8':
        func.show_book(books)
    else:
        print("The given command doesnt exist...")
    input("Press enter to continue...")
    system('cls')
    func.print_options()
    
    option = input()

print("Bye!")