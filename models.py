class Book:
    def __init__(self, book_id, title, author_id, genre_id, publication_date, available=True):
        self._book_id = book_id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.publication_date = publication_date
        self.available = available

    @property
    def book_id(self):
        return self._book_id

    def update_availability(self, is_available):
        self.available = is_available
        print(f"Updated availability for {self.title} to {'available' if is_available else 'not available'}.")

    def __str__(self):
        return f"Book({self.title}, ISBN: {self.isbn})"

class User:
    def __init__(self, user_id, name, email, phone, address, username, password):
        self._user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.username = username
        self.password = password

    @property
    def user_id(self):
        return self._user_id

    def update_contact_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        print(f"Updated contact info for {self.name}.")

    def __str__(self):
        return f"User(Name: {self.name}, Username: {self.username}, Email: {self.email})"


class Author:
    def __init__(self, author_id, name, biography):
        self._author_id = author_id
        self.name = name
        self.biography = biography

    @property
    def author_id(self):
        return self._author_id

    def update_biography(self, biography):
        self.biography = biography
        print(f"Updated biography for {self.name}.")

    def __str__(self):
        return f"Author({self.name})"

class Genre:
    def __init__(self, genre_id, name, description):
        self._genre_id = genre_id
        self.name = name
        self.description = description

    @property
    def genre_id(self):
        return self._genre_id

    def update_description(self, description):
        self.description = description
        print(f"Updated description for genre {self.name}.")

    def __str__(self):
        return f"Genre({self.name})"

class BorrowedBook:
    def __init__(self, borrowed_id, book_id, user_id, borrow_date, return_date):
        self._borrowed_id = borrowed_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    @property
    def borrowed_id(self):
        return self._borrowed_id

    def extend_return_date(self, new_date):
        self.return_date = new_date
        print(f"Extended return date for book ID {self.book_id}.")

    def __str__(self):
        return f"BorrowedBook(Book ID: {self.book_id}, Due: {self.return_date})"
