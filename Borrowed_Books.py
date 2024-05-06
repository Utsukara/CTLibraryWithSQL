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
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO borrowed_books(book, user, borrowed_date, return_date) VALUES(%s, %s, %s, %s)",
                           (self.book, self.user, self.borrowed_date, self.return_date))
            connection.commit()
            print("Borrowed book added successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def Return_Borrowed_Book():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM borrowed_books WHERE borrowed_id = %s", (self.borrowed_id,))
            connection.commit()
            print("Borrowed book returned successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close() 

    def View_Borrowed_Book_Details():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM borrowed_books WHERE borrowed_id = %s", (self.borrowed_id,))
            record = cursor.fetchone()
            print("Borrowed ID: ", record[0])
            print("Book: ", record[1])
            print("User: ", record[2])
            print("Borrowed Date: ", record[3])
            print("Return Date: ", record[4])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def Display_All_Borrowed_Books():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM borrowed_books")
            records = cursor.fetchall()
            for record in records:
                print("Borrowed ID: ", record[0])
                print("Book: ", record[1])
                print("User: ", record[2])
                print("Borrowed Date: ", record[3])
                print("Return Date: ", record[4])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()