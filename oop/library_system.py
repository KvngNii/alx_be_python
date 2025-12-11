class Book:
    """
    Base class representing a book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book class.
    
    Attributes:
        title (str): The title of the book (inherited)
        author (str): The author of the book (inherited)
        file_size (int): The file size of the ebook in KB
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book class.
    
    Attributes:
        title (str): The title of the book (inherited)
        author (str): The author of the book (inherited)
        page_count (int): The number of pages in the book
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """
    Class representing a library that manages a collection of books.
    Demonstrates composition by containing Book instances.
    
    Attributes:
        books (list): A list to store Book, EBook, and PrintBook instances
    """
    
    def __init__(self):
        """
        Initialize a Library instance with an empty books list.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
