import my_functions as func
import os


option = ''
books = []

while option != 'X':
    if option == '1':
        book = func.create_book()
        books.append(book)
        input("Command executed... press any button to continue")
    elif option == '2':
        func.save_books(books)
        input("Books where saved... press any button to continue")
    os.system('cls')
    print("\nBook Store\n")
    func.print_options()
    print("\n")

    option = input("Enter your option: ").upper()
print("Bye!")