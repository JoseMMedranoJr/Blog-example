# Inheritance

#  Instance, Class, and Static

#  Getters and setters 

class Book:
    #  class attributes Go here
    #  instance attributes defined in init
    #  two attributes: titel and author
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    # class method called create_book
    #  are referenced in relation to the CLASS itself

    @classmethod
    def create_book_cslewis(cls, new_title):
        return cls(new_title, "C. S. Lewis")

# default "blanks": 
# nubmbers: 0
# string: "" (blandk string)
# bool: Treu or False (depending on what you use)
# list: = []
# dict: {}
# anything else: None

class LibraryUser:
    #  calss variables go before init method
    number_of_users = 0
    

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email
        self.has_book = False
        self.borrow_book = None # value is non-existent
        LibraryUser.number_of_users += 1
        #  whenever we create a new user, we need to nuber_of_users ++

    # This is an instance method
    # This function checks out a book per user
    #  Has the user already checked out a book?
        #  if they have, they cant check out a another one -- throw error/print something
        #  if the user has not checked out a book yet
            # store the borrowed book as an instance attribute
            #  print our a confirmation message for the user.

    def borrow_book(self, book):
        if self.has_book:# has_book is either True or False
            print("You already have one book checked out. You can't check out any more.")
        else: 
            self.has_book = True # updates user to have checked out a book
            self.borrowed = book
            book_title = book.title
            print(f"Congrats, you've check out {book_title}!") 


    @classmethod
    #  get total number of users in system - CLASS
    def get_user_count(cls):
        return cls.number_of_users

class Librarian(LibraryUser):
    
    listOfBooks = []

    def __init__(self, user_name, email):
        super().__init__(user_name, email)

    def add_book_to_library(self, book):
        Librarian.listOfBooks.append(Book)




user_danny = LibraryUser("Danny", "danny@dan.com")

user_danny.borrow_book(testbook)

testbook = Book("test", "test author")
testbook_narnia = Book.create_book_cslewis("Narnia")
# testbook.title = 
print(LibraryUser.get_user_count())


# user_set_title = input("Give me an author name")
# user_set_name = input("Giver me an author name")