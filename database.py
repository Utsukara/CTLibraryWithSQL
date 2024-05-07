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
    def add_new_book(self, title, author_id, genre_id, isbn, publication_date):
        query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        self.execute_query(query, (title, author_id, genre_id, isbn, publication_date))
        print("Book added successfully.")

    def remove_book(self, book_id):
        self.execute_query("DELETE FROM books WHERE id = %s", (book_id,))
        print("Book removed successfully.")

    def search_books(self, keyword):
        results = self.fetch_all("SELECT * FROM books WHERE title LIKE %s OR isbn LIKE %s", ('%' + keyword + '%', '%' + keyword + '%'))
        for result in results:
            print(result)

    def display_all_books(self):
        results = self.fetch_all("SELECT * FROM books", None)
        for result in results:
            print(result)

    def update_book(self, book_id, title=None, author_id=None, genre_id=None, isbn=None, publication_date=None):
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
        if isbn:
            updates.append("isbn = %s")
            params.append(isbn)
        if publication_date:
            updates.append("publication_date = %s")
            params.append(publication_date)
        params.append(book_id)
        query = f"UPDATE books SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Book updated successfully.")

    # Author operations
    def add_new_author(self, name, biography):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        self.execute_query(query, (name, biography))
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

    # Genre operations
    def add_new_genre(self, name, description, category):
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        self.execute_query(query, (name, description, category))
        print("Genre added successfully.")

    def remove_genre(self, genre_id):
        self.execute_query("DELETE FROM genres WHERE id = %s", (genre_id,))
        print("Genre removed successfully.")

    def display_all_genres(self):
        results = self.fetch_all("SELECT * FROM genres", None)
        for result in results:
            print(result)

    def update_genre(self, genre_id, name=None, description=None, category=None):
        updates = []
        params = []
        if name:
            updates.append("name = %s")
            params.append(name)
        if description:
            updates.append("description = %s")
            params.append(description)
        if category:
            updates.append("category = %s")
            params.append(category)
        params.append(genre_id)
        query = f"UPDATE genres SET {', '.join(updates)} WHERE id = %s"
        self.execute_query(query, params)
        print("Genre updated successfully.")

    # User operations
    def add_new_user(self, name, email, phone, address, password):
        query = "INSERT INTO users (name, email, phone, address, password) VALUES (%s, %s, %s, %s, %s)"
        self.execute_query(query, (name, email, phone, address, password))
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

    def authenticate_customer(self, username, password):
        query = "SELECT id FROM users WHERE username = %s AND password = %s"
        results = self.perform_database_operation(query, (username, password), fetch=True)
        if results:
            return results[0][0]  #return customer ID
        return None
    
    def register_new_customer(self, name, email, phone, address, username, password):
        # Check if username or email already exists to avoid duplicates
        check_query = "SELECT EXISTS(SELECT 1 FROM users WHERE username=%s OR email=%s)"
        exists = self.fetch_all(check_query, (username, email))
        if exists[0][0]:
            print("Username or email already exists. Please try a different one.")
            return False

        # Insert new user into the database
        query = "INSERT INTO users (name, email, phone, address, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            self.execute_query(query, (name, email, phone, address, username, password))
            print("New customer registered successfully.")
            return True
        except Error as e:
            print(f"Error registering new customer: {e}")
            return False
