class Book:
    #PUBLIC BookName : STRING
    #PUBLIC AuthorName : STRING
    #PUBLIC ISBN : INTEGER
    def __init__(self, BookNameP, AuthorNameP, ISBNP):  #P for Parameter
        self.BookName = BookNameP	#self. instead of self.__ as we want public and not private declaration
        self.AuthorName = AuthorNameP
        self.ISBN = ISBNP

MyBook = Book("Automate the Boring Stuff With Python", "Al", "015732")
print(MyBook.BookName)
print(MyBook.AuthorName)
MyBook.AuthorName = "Sweigart"
print(MyBook.AuthorName)