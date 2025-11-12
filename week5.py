# Library Management System using OOP

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # True means the book can be borrowed

    def __str__(self):
        status = "Available" if self.is_available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def __str__(self):
        borrowed = ', '.join([b.title for b in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name} (ID: {self.member_id}) | Books: {borrowed}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered in the library.")

    def display_books(self):
        print(f"\n📚 Books in {self.name}:")
        for book in self.books:
            print(book)

    def display_members(self):
        print(f"\n👥 Members of {self.name}:")
        for member in self.members:
            print(member)


# ----------------------------
# Example Usage
# ----------------------------

# Create a library
library = Library("City Library")

# Add books
book1 = Book("Harry Potter", "J.K. Rowling", "12345")
book2 = Book("The Alchemist", "Paulo Coelho", "67890")
library.add_book(book1)
library.add_book(book2)

# Add members
member1 = Member("Rohit Yadav", "M001")
member2 = Member("Sneha Sharma", "M002")
library.add_member(member1)
library.add_member(member2)

# Borrow and return books
member1.borrow_book(book1)
member2.borrow_book(book1)  # Already borrowed
member1.return_book(book1)
member2.borrow_book(book1)

# Display status
library.display_books()
library.display_members()

