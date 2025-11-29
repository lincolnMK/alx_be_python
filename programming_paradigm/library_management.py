class Book:
    _isChecked_out = False

    def __init__(self, title, author ):
        self.title = title
        self.author = author
        
        


class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_available_books(self):
        for book in self.books:
            if not book._isChecked_out:
                print(book.get_summary())
                
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book._isChecked_out:
                book._isChecked_out = True
                print(f"You have checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")
        
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._isChecked_out:
                book._isChecked_out = False
                print(f"You have returned '{title}'.")
                return
        print(f"'{title}' was not checked out.")
