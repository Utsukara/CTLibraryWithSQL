import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = None
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            self.disconnect()

    def fetch_all(self, query, params=None):
        cursor = None
        results = []
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
        finally:
            if cursor:
                cursor.close()
            self.disconnect()
        return results



    # Book operations
    def add_new_book(self, title, author_id, genre_id, publication_date):
        query = "INSERT INTO books (title, author_id, genre_id, publication_date) VALUES (%s, %s, %s, %s)"
        self.execute_query(query, (title, author_id, genre_id, publication_date))
        print("Book added successfully.")

    def remove_book(self, book_id):
        self.execute_query("DELETE FROM books WHERE id = %s", (book_id,))
        print("Book removed successfully.")

    def search_books(self, keyword):
        results = self.fetch_all("SELECT * FROM books WHERE title LIKE %s", ('%' + keyword + '%',))
        for result in results:
            print(result)

    def display_all_books(self):
        results = self.fetch_all("SELECT * FROM books", None)
        for result in results:
            print(result)

    def update_book(self, book_id, title=None, author_id=None, genre_id=None, publication_date=None):
        updates = []
        params = []
        if title:
            updates.append("title = %s")
            params.append(title)
        if author_id:
            updates.append("author_id = %s")
            params.append(author_id)
        if genre_id:
            updates.append("genre_id = %s")
            params.append(genre_id)
        if publication_date:
            updates.append("publication_date = %s")
            params.append(publication_date)
        params.append(book_id)
        query = f"UPDATE books SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Book updated successfully.")



    # Author operations
    def add_new_author(self, name, biography=''):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        self.execute_query(query, (name, biography or 'No biography provided'))
        print("Author added successfully.")

    def remove_author(self, author_id):
        self.execute_query("DELETE FROM authors WHERE id = %s", (author_id,))
        print("Author removed successfully.")

    def display_all_authors(self):
        results = self.fetch_all("SELECT * FROM authors", None)
        for result in results:
            print(result)

    def update_author(self, author_id, name=None, biography=None):
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if biography:
            updates.append("biography = %s")
            params.append(biography)
        params.append(author_id)
        query = f"UPDATE authors SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Author updated successfully.")

    def find_or_add_author(self, author_name):
        author_id = self.fetch_all("SELECT id FROM authors WHERE name = %s", (author_name,))
        if not author_id:
            self.execute_query("INSERT INTO authors (name, biography) VALUES (%s, '')", (author_name,))
            author_id = self.fetch_all("SELECT id FROM authors WHERE name = %s", (author_name,))
        return author_id[0][0]



    # Genre operations
    def add_new_genre(self, name, description=None):
        description = description if description is not None else 'No description provided'
        query = "INSERT INTO genres (name, description) VALUES (%s, %s)"
        self.execute_query(query, (name, description))
        print("Genre added successfully.")

    def remove_genre(self, genre_id):
        self.execute_query("DELETE FROM genres WHERE id = %s", (genre_id,))
        print("Genre removed successfully.")

    def display_all_genres(self):
        results = self.fetch_all("SELECT id, name, description FROM genres", None)
        for result in results:
            print(f"ID: {result[0]}, Name: {result[1]}, Description: {result[2]}")

    def update_genre(self, genre_id, name=None, description=None):
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if description:
            updates.append("description = %s")
            params.append(description)
        if not updates:
            print("No updates provided.")
            return
        params.append(genre_id)
        query = f"UPDATE genres SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Genre updated successfully.")

    def find_or_add_genre(self, genre_name, description=None):
        genre_id = self.fetch_all("SELECT id FROM genres WHERE name = %s", (genre_name,))
        if not genre_id:
            description = description if description else 'No description provided'
            self.execute_query("INSERT INTO genres (name, description) VALUES (%s, %s)", (genre_name, description))
            genre_id = self.fetch_all("SELECT id FROM genres WHERE name = %s", (genre_name,))
            print(f"Genre '{genre_name}' added successfully.")
        return genre_id[0][0]


    # User operations
    def add_new_user(self, name, email, phone, address, username, password):
        query = "INSERT INTO users (name, email, phone, address, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
        self.execute_query(query, (name, email, phone, address, username, password))
        print("User added successfully.")

    def remove_user(self, user_id):
        self.execute_query("DELETE FROM users WHERE id = %s", (user_id,))
        print("User removed successfully.")

    def display_all_users(self):
        results = self.fetch_all("SELECT * FROM users", None)
        for result in results:
            print(result)

    def update_user(self, user_id, name=None, email=None, phone=None, address=None, password=None):
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if email:
            updates.append("email = %s")
            params.append(email)
        if phone:
            updates.append("phone = %s")
            params.append(phone)
        if address:
            updates.append("address = %s")
            params.append(address)
        if password:
            updates.append("password = %s")
            params.append(password)
        params.append(user_id)
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("User updated successfully.")

    def authenticate_user(self, username, password):
        # implement hashing for password in future implementations
        query = "SELECT id FROM users WHERE username = %s AND password = %s"
        results = self.fetch_all(query, (username, password))
        if results:
            return results[0][0]
        else:
            return None
        
    def borrow_book(self, book_id, username):
        user_id = self.fetch_all("SELECT id FROM users WHERE username = %s", (username,))
        if user_id:
            available = self.fetch_all("SELECT available FROM books WHERE id = %s", (book_id,))
            if available and available[0][0]:
                return_date = datetime.now() + timedelta(days=14)
                self.execute_query("UPDATE books SET available = 0 WHERE id = %s", (book_id,))
                self.execute_query("INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date) VALUES (%s, %s, CURDATE(), %s)", (book_id, user_id[0][0], return_date.strftime('%Y-%m-%d')))
                print("Book borrowed successfully. Return by: ", return_date.strftime('%Y-%m-%d'))
            else:
                print("This book is currently unavailable.")
        else:
            print("User not found.")

    def return_book(self, book_id, username):
        user_id = self.fetch_all("SELECT id FROM users WHERE username = %s", (username,))
        if user_id:
            borrowed = self.fetch_all("SELECT id FROM borrowed_books WHERE book_id = %s AND user_id = %s", (book_id, user_id[0][0]))
            if borrowed:
                self.execute_query("UPDATE books SET available = 1 WHERE id = %s", (book_id,))
                self.execute_query("DELETE FROM borrowed_books WHERE id = %s", (borrowed[0][0],))
                print("Book returned successfully.")
            else:
                print("This book was not borrowed by you or does not exist.")
        else:
            print("User not found.")

    def view_borrowed_books(self, username):
        user_id = self.fetch_all("SELECT id FROM users WHERE username = %s", (username,))
        if user_id:
            results = self.fetch_all("SELECT b.title, bb.borrow_date, bb.return_date FROM borrowed_books bb JOIN books b ON bb.book_id = b.id WHERE bb.user_id = %s", (user_id[0][0],))
            for result in results:
                print(f"Title: {result[0]}, Borrowed on: {result[1]}, Return by: {result[2]}")
        else:
            print("User not found.")

    def view_customer_account(self, username):
        results = self.fetch_all("SELECT name, email, phone, address FROM users WHERE username = %s", (username,))
        if results:
            print(f"Name: {results[0][0]}, Email: {results[0][1]}, Phone: {results[0][2]}, Address: {results[0][3]}")
        else:
            print("User not found.")
