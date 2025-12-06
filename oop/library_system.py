class Book:
    def  __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            if isinstance(book, Book) and not isinstance(book, (EBook, PrintBook)):
                print(f"Book: {book}")
            if isinstance(book, EBook):
                print(f"EBook: {book}, File Size: {book.file_size}KB")
            if isinstance(book, PrintBook):
                print(f"Print Book: {book}, Page Count: {book.page_count}")
            
