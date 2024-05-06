import sql.connector
from sql.connector import Error

import Book


class User:
    def __init__(self, user_id, user_name, user_email, user_phone, user_address, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_address = user_address
        self.user_password = user_password


    def Add_New_User():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users(user_name, user_email, user_phone, user_address, user_password) VALUES(%s, %s, %s, %s, %s)",
                           (self.user_name, self.user_email, self.user_phone, self.user_address, self.user_password))
            connection.commit()
            print("User added successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def View_User_Details():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (self.user_id,))
            record = cursor.fetchone()
            print("User ID: ", record[0])
            print("User Name: ", record[1])
            print("User Email: ", record[2])
            print("User Phone: ", record[3])
            print("User Address: ", record[4])
            print("User Password: ", record[5])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def Display_All_Users():
        try:
            connection = sql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='password')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()
            for record in records:
                print("User ID: ", record[0])
                print("User Name: ", record[1])
                print("User Email: ", record[2])
                print("User Phone: ", record[3])
                print("User Address: ", record[4])
                print("User Password: ", record[5])
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()