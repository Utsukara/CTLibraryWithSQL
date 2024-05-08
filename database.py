import mysql.connector
from mysql.connector import Error

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
    def add_new_author(self, name):
        query = "INSERT INTO authors (name, biography) VALUES (%s, '')"
        self.execute_query(query, (name,))
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
    def add_new_genre(self, name, description=''):
        query = "INSERT INTO genres (name, description) VALUES (%s, %s)"
        self.execute_query(query, (name, description))
        print("Genre added successfully.")

    def remove_genre(self, genre_id):
        self.execute_query("DELETE FROM genres WHERE id = %s", (genre_id,))
        print("Genre removed successfully.")

    def display_all_genres(self):
        results = self.fetch_all("SELECT * FROM genres", None)
        for result in results:
            print(result)

    def update_genre(self, genre_id, name=None, description=None):
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if description:
            updates.append("description = %s")
            params.append(description)
        params.append(genre_id)
        query = f"UPDATE genres SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Genre updated successfully.")

    def find_or_add_genre(self, genre_name):
        genre_id = self.fetch_all("SELECT id FROM genres WHERE name = %s", (genre_name,))
        if not genre_id:
            self.execute_query("INSERT INTO genres (name, description) VALUES (%s, '')", (genre_name,))
            genre_id = self.fetch_all("SELECT id FROM genres WHERE name = %s", (genre_name,))
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
