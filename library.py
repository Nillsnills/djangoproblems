class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return self.title
    def borrow(self):
        self.available = False
    def return_book(self):
        self.available = True



class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
    def __str__(self):
        return self.name
    def borrow_book(self, book):
        self.borrowed_books = []
        self.borrowed_books.append(book)
        book.borrow()
    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()



class Library:
    def __init__(self, books=[], members=[]):
        self.books = books
        self.members = members
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)      
    def issue_book(self, member_id, isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        member.borrow_book(book)
    def return_book(self, member_id, isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        member.return_book(book)




book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")
print(book1)
print(book2)

library = Library()
library.add_book(book1)
library.add_book(book2)


member = Member("آلیس", "M001")
library.register_member(member)
print(member)


library.issue_book("M001", "1234567890")
print(book1.available)

library.return_book("M001", "1234567890")
print(book1.available)

