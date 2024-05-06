import sql.connector
from sql.connector import Error

import Author
import Genre
import User

class Book:
    def __init__(self, book_id, book_name, author, genre, user, book_status):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.user = user
        self.book_status = book_status

    def Add_New_Book():
        pass

    def View_Book_Details():
        pass

    def Display_All_Books():
        pass