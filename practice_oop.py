class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed {book.title}"
        return f"{book.title} is not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}"
        return f"{self.name} does not have {book.title}"

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if member and book:
            return member.return_book(book)
        return False

    def __str__(self):
        books_info = [str(book) for book in self.books]
        members_info = [str(member) for member in self.members]
        return f"Books:\n{', '.join(books_info)}\nMembers:\n{', '.join(members_info)}"


def main():
    # Create library
    library = Library()

    # Add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register members
    member1 = Member("Alice", 101)
    member2 = Member("Bob", 102)
    library.register_member(member1)
    library.register_member(member2)

    # Lend books to members
    library.lend_book(101, "The Great Gatsby")
    library.lend_book(102, "To Kill a Mockingbird")
    library.lend_book(101, "1984")

    # Return books
    library.return_book(101, "The Great Gatsby")
    library.return_book(102, "To Kill a Mockingbird")

    # Display library information
    print(library)

if __name__ == '__main__':
    main()
