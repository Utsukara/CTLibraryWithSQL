-- Create table for Authors
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- Create table for Genres
CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50)
);

-- Create table for Books
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    publication_date DATE,
    available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

-- Create table for Users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT,
    password VARCHAR(255) NOT NULL
);

-- Create table for Borrowed Books (if needed)
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    user_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert data into Authors table
INSERT INTO authors (name, biography) VALUES
('J.K. Rowling', 'Author of the Harry Potter series.'),
('George Orwell', 'Author known for dystopian novels.'),
('Agatha Christie', 'Famous for her detective novels.');

-- Insert data into Genres table
INSERT INTO genres (name, description, category) VALUES
('Fantasy', 'Genre involving magical or supernatural elements.', 'Fiction'),
('Science Fiction', 'Genre dealing with futuristic concepts.', 'Fiction'),
('Mystery', 'Genre involving suspense and investigation.', 'Fiction');

-- Insert data into Books table
INSERT INTO books (title, author_id, genre_id, isbn, publication_date, available) VALUES
('Harry Potter and the Sorcerer\'s Stone', 1, 1, '9780747532743', '1997-06-26', TRUE),
('1984', 2, 2, '9780451524935', '1949-06-08', TRUE),
('Murder on the Orient Express', 3, 3, '9780425200452', '1934-01-01', TRUE);

-- Insert data into Users table
INSERT INTO users (name, email, phone, address, password) VALUES
INSERT INTO users (name, username, email, phone, address, password) VALUES
('Alice Johnson', 'alicejohnson', 'alice.johnson@example.com', '1234567890', '123 Maple Street', 'alicepassword'),
('Bob Smith', 'bobsmith', 'bob.smith@example.com', '2345678901', '456 Oak Avenue', 'bobpassword'),
('Carol White', 'carolwhite', 'carol.white@example.com', '3456789012', '789 Pine Road', 'carolpassword'),
('David Brown', 'davidbrown', 'david.brown@example.com', '4567890123', '1012 Cedar Lane', 'davidpassword'),
('Eve Black', 'eveblack', 'eve.black@example.com', '5678901234', '1314 Spruce Blvd', 'evepassword');


-- Insert data into Borrowed Books table (track book loans)
INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date) VALUES
(1, 1, '2023-01-01', '2023-01-31'),
(2, 2, '2023-01-05', '2023-02-05');
