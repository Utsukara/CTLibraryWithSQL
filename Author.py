import sql.connector
from sql.connector import Error

import Book
import Genre


class Author:
    def __init__(self, author_id, author_name, author_description):
        self.author_id = author_id
        self.author_name = author_name
        self.author_description = author_description



    def Add_New_Author():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO authors(author_name, author_description) VALUES(%s, %s)",
                           (self.author_name, self.author_description))
            connection.commit()
            print("Author added successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def View_Author_Details():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM authors WHERE author_id = %s", (self.author_id,))
            record = cursor.fetchone()
            print("Author ID: ", record[0])
            print("Author Name: ", record[1])
            print("Author Description: ", record[2])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def Display_All_Authors():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM authors")
            records = cursor.fetchall()
            for record in records:
                print("Author ID: ", record[0])
                print("Author Name: ", record[1])
                print("Author Description: ", record[2])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()