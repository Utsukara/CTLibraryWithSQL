import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def perform_database_operation(self, query, params=None, fetch=False):
        """General database operation function to execute queries."""
        results = []
        try:
            with mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    if fetch:
                        results = cursor.fetchall()
                    connection.commit()
        except Error as e:
            print(f"Error: {e}")
        return results

    # Book operations
    def add_new_book(self, title, author_id, genre_id, publication_date):
        query = "INSERT INTO books (title, author_id, genre_id, publication_date) VALUES (%s, %s, %s, %s, %s)"
        self.perform_database_operation(query, (title, author_id, genre_id, publication_date))
        print("Book added successfully.")

    def remove_book(self, book_id):
        query = "DELETE FROM books WHERE id = %s"
        self.perform_database_operation(query, (book_id,))
        print("Book removed successfully.")

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
        self.perform_database_operation(query, params)
        print("Book updated successfully.")

    def search_books(self, keyword):
        query = "SELECT * FROM books WHERE title LIKE %s"
        results = self.perform_database_operation(query, ('%' + keyword + '%', '%' + keyword + '%'), fetch=True)
        for result in results:
            print(result)

    def display_all_books(self):
        query = "SELECT * FROM books"
        results = self.perform_database_operation(query, fetch=True)
        for result in results:
            print(result)

    # Author operations
    def add_new_author(self, name, biography):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        self.perform_database_operation(query, (name, biography))
        print("Author added successfully.")

    def remove_author(self, author_id):
        query = "DELETE FROM authors WHERE id = %s"
        self.perform_database_operation(query, (author_id,))
        print("Author removed successfully.")

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
        self.perform_database_operation(query, params)
        print("Author updated successfully.")

    def display_all_authors(self):
        query = "SELECT * FROM authors"
        results = self.perform_database_operation(query, fetch=True)
        for result in results:
            print(result)

    # Genre operations
    def add_new_genre(self, name, description, category):
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        self.perform_database_operation(query, (name, description, category))
        print("Genre added successfully.")

    def remove_genre(self, genre_id):
        query = "DELETE FROM genres WHERE id = %s"
        self.perform_database_operation(query, (genre_id,))
        print("Genre removed successfully.")

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
        self.perform_database_operation(query, params)
        print("Genre updated successfully.")

    # User operations
    def add_new_user(self, name, email, phone, address, password):
        query = "INSERT INTO users (name, email, phone, address, password) VALUES (%s, %s, %s, %s, %s)"
        self.perform_database_operation(query, (name, email, phone, address, password))
        print("User added successfully.")

    def remove_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.perform_database_operation(query, (user_id,))
        print("User removed successfully.")

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
        self.perform_database_operation(query, params)
        print("User updated successfully.")

    def display_all_users(self):
        query = "SELECT * FROM users"
        results = self.perform_database_operation(query, fetch=True)
        for result in results:
            print(result)