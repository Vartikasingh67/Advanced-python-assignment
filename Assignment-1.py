class Library:

    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added successfully!")

    def register_patron(self):
        name = input("Enter patron name: ")
        self.patrons.append(name)
        print("Patron registered successfully!")

    def borrow_book(self):
        name = input("Enter patron name: ")
        book = input("Enter book name to borrow: ")

        if name in self.patrons and book in self.books:
            self.books.remove(book)
            print(name, "borrowed", book)
        else:
            print("Book or Patron not found!")

    def return_book(self):
        book = input("Enter book name to return: ")
        self.books.append(book)
        print("Book returned successfully!")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
