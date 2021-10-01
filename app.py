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
        print(f"Books loaded: {len(books)}")
    else:
        print("The given command doesnt exist...")
    input("Press enter to continue...")
    os.system('cls')
    func.print_options()
    
    option = input()

print("Bye!")