import sql.connector
from sql.connector import Error

import Author
import Book


class Genre:
    def __init__(self, genre_id, genre_name, genre_description):
        self.genre_id = genre_id
        self.genre_name = genre_name
        self.genre_description = genre_description

    def Add_New_Genre():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO genres(genre_name, genre_description) VALUES(%s, %s)",
                           (self.genre_name, self.genre_description))
            connection.commit()
            print("Genre added successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def View_Genre_Details():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM genres WHERE genre_id = %s", (self.genre_id,))
            record = cursor.fetchone()
            print("Genre ID: ", record[0])
            print("Genre Name: ", record[1])
            print("Genre Description: ", record[2])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def Display_All_Genres():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM genres")
            records = cursor.fetchall()
            for record in records:
                print("Genre ID: ", record[0])
                print("Genre Name: ", record[1])
                print("Genre Description: ", record[2])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()