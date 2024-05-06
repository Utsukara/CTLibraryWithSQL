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
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO books(book_name, author_id, genre_id, user_id, book_status) VALUES(%s, %s, %s, %s, %s)",
                           (self.book_name, self.author, self.genre, self.user, self.book_status))
            connection.commit()
            print("Book added successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def View_Book_Details():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books WHERE book_id = %s", (self.book_id,))
            record = cursor.fetchone()
            print("Book ID: ", record[0])
            print("Book Name: ", record[1])
            print("Author: ", record[2])
            print("Genre: ", record[3])
            print("User: ", record[4])
            print("Book Status: ", record[5])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def Display_All_Books():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            records = cursor.fetchall()
            for record in records:
                print("Book ID: ", record[0])
                print("Book Name: ", record[1])
                print("Author: ", record[2])
                print("Genre: ", record[3])
                print("User: ", record[4])
                print("Book Status: ", record[5])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()