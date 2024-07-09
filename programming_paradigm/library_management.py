class Book:
    def __init__(self, title, author):
        """
        Initializes a new book with a title, author, and sets its checked-out status to False.
        """
        self.title = title 
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        self._is_checked_out = False 
    
    def is_available(self):
        """
        Returns True if the book is available (not checked out), otherwise False.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the book. 
        """
        return f"{self.title} by {self.author}"



class Library:
    def __init__(self):
        """
        Initializes a new library with an empty list of books. 
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a new book to the library's collection. 
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title if it is available.
        Prints a message indicating the success or failure of the operation.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f'Book "{title}" has been checked out.')
                return
            print(f'Book "{title}" is not available.')

    def return_book(self, title):
        """
        Returns a book by title if it was checked out.
        Prints a message indicating the success or failure of the operation.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f'Book "{title}" has been returned.')
                return
        print(f'Book "{title}" was not checked out.')


    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
