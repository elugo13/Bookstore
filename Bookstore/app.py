import my_functions as func
import os


func.print_options()
option = input()
books = []

while option.upper() != 'X':
    if option == '1':
        book = func.create_book()
        books.append(book)
    elif option == '2':
        func.save_books(books)
    elif option == '3':
        books = func.load_books()
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
    os.system('cls')
    func.print_options()
    
    option = input()

print("Bye!")