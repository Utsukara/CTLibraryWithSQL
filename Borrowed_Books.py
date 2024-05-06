import sql.connector
from sql.connector import Error

import Book

class Borrowed_Books:
    def __init__(self, borrowed_id, book, user, borrowed_date, return_date):
        self.borrowed_id = borrowed_id
        self.book = book
        self.user = user
        self.borrowed_date = borrowed_date
        self.return_date = return_date

    def Add_New_Borrowed_Book():
        pass

    def View_Borrowed_Book_Details():
        pass

    def Display_All_Borrowed_Books():
        pass