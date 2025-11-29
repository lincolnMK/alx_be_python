class Book:
    _isChecked_out = False

    def __init__(self, title, author ):
        self.title = title
        self.author = author
        
        
    def get_summary(self):
        return f"'{self.title}' by {self.author}"
    

class Library:
    def __init__(self):
        self.books = []
        
    def availability_status(self):
        return "Available" if not self._isChecked_out else "Checked Out"
    
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        
    def list_books(self):
        return [book.get_summary() for book in self.books]
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book._isChecked_out = False
                return f"'{title}' has been returned."
        return f"'{title}' not found in the library."
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book._isChecked_out:
                    book._isChecked_out = True
                    return f"You have checked out '{title}'."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' not found in the library."
    def list_available_books(self):
        available_books = [book.get_summary() for book in self.books if not book._isChecked_out]
        for summary in available_books:
            print(summary)