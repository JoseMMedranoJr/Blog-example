# Inheritance - football plays

# Instance, Class, and Static Methods

# Getters and Setters


class Book:
    # CLASS ATTRIBUTES GO HERE


    # INSTANCE ATTRIBUTES DEFINED IN INIT
    def __init__(self, title, author):
        self.title = title
        self.author = author


    # class method called create_book
    # are referenced in relation to the CLASS itself

    @classmethod
    def create_book_cslewis(cls, new_title):
        return cls(new_title, "C. S. Lewis")





testbook = Book("test", "test author")

testbook_narnia = Book.create_book_cslewis("Narnia") # automatically sets the author to C. S. Lewis


# default "blanks"/placeholder values:
    # number: 0
    # string: "" (blank string)
    # bool: True OR False (depending on what you use)
    # list: []
    # dict: {}
    # anything else: None









class LibraryUser:

    number_of_users = 0 # this is a CLASS variable
    

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.has_book = False # sets the initial value for has_book
        self.borrowed_book = None # sets the initial value for borrowed_book

        # whenever we CREATE a new user, we need to number_of_users ++
        LibraryUser.number_of_users += 1

    
    # this is an INSTANCE method
    # this function checks out a book for the user
    # has the user already checked out a book?
        # if they have, they can't check out another one -- throw error/print something
    # if the user has not checked out a book yet
        # store the borrowed book as an instance attribute
        # print out a confirmation message for the user

    def borrow_book(self, book):
        if self.has_book: # has_book is either True or False
            print("You already have one book checked out. You can't check out any more.")
        else:
            self.has_book = True # updates user to have checked out a book
            self.borrowed_book = book

            book_title = book.title
            print(f"Congratulations! You have checked out {book_title}.")


    @classmethod
    # return total number of users in the system
    def get_user_count(cls):
        return cls.number_of_users

    

class Librarian(LibraryUser):
    
    listOfBooks = [] # this is a CLASS attribute

    def __init__(self, user_name, email):
        super().__init__(user_name, email)


    def add_book_to_library(self, book):
        Librarian.listOfBooks.append(book)


user_danny = LibraryUser("Danny", "danny@dan.com")
# danny wants to check out testbook

user_danny.borrow_book(testbook)

print(LibraryUser.get_user_count())


user_tony = LibraryUser("Tony", "tony@tony.tony")

print(LibraryUser.get_user_count())