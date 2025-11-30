class Book:
    

    def __init__(self, title, author, _is_checked_out = False ):
        self.title = title
        self.author = author
        self._isChecked_out = _is_checked_out

    def check_out_book(self):
        if not self._isChecked_out:
            self._isChecked_out = True
            print(f"Checked out: {self.title}")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def return_book(self):
        if self._isChecked_out:
            self._isChecked_out = False
            print(f"Returned: {self.title}")
        else:
            print(f"Book '{self.title}' was not checked out.")

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            if not book._isChecked_out:
                print(f"{book.title} by {book.author}")
                
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")
