class UserInterface:
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def display_initial_menu():
        print("Welcome to the Library Management System!")
        print("1. Customer")
        print("2. Librarian")
        print("3. New Customer")
        print("4. Quit")

    @staticmethod
    def handle_initial_menu(database_manager):
        while True:
            UserInterface.display_initial_menu()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                UserInterface.handle_customer_sign_in(database_manager)
            elif choice == "2":
                UserInterface.handle_librarian_sign_in(database_manager)
            elif choice == "3":
                UserInterface.handle_new_customer_sign_up(database_manager)
            elif choice == "4":
                print("Exiting system...")
                exit()
            else:
                print("Invalid choice. Please try again.")


    def handle_customer_sign_in(database_manager):
        username = UserInterface.get_user_input("Enter your username: ")
        password = UserInterface.get_user_input("Enter your password: ")
        customer_id = database_manager.authenticate_user(username, password)
        if customer_id:
            print(f"Welcome Customer#{customer_id}! Login Successful")
            UserInterface.handle_customer_menu(database_manager)
        else:
            print("Login failed. Please check your username and password.")


    def handle_librarian_sign_in(database_manager):
        password = UserInterface.get_user_input("Enter librarian password: ")
        # Assuming a static password check for demonstration; consider a more secure approach for production
        if password == "librarian123":  # Example of hard-coded password (not recommended for real systems)
            print("Librarian access granted.")
            UserInterface.handle_librarian_main_menu(database_manager)
        else:
            print("Access denied. Incorrect password.")

    @staticmethod
    def handle_new_customer_sign_up(database_manager):
        name = UserInterface.get_user_input("Enter your name: ")
        email = UserInterface.get_user_input("Enter your email: ")
        phone = UserInterface.get_user_input("Enter your phone number: ")
        address = UserInterface.get_user_input("Enter your address(optional): ")
        username = UserInterface.get_user_input("Choose a username: ")
        password = UserInterface.get_user_input("Choose a password: ")
        if database_manager.register_new_customer(name, email, phone, address, username, password):
            print("Registration successful. You can now log in as a customer.")
            print("Returning to the main menu...")
            UserInterface.handle_initial_menu(database_manager)
        else:
            print("Registration failed. Please try again.")

    @staticmethod
    def customer_menu(database_manager):
        print("Customer Menu:")
        print("1. Browse books")
        print("2. Borrow books")
        print("3. Return books")
        print("4. View my borrowed books")
        print("5. My account")
        print("6. Logout")

    def handle_customer_menu(database_manager):
        while True:
            UserInterface.customer_menu(database_manager)
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                database_manager.display_all_books()
            elif choice == "2":
                book_id = int(UserInterface.get_user_input("Enter the ID of the book you want to borrow: "))
                username = UserInterface.get_user_input("Enter your username: ")
                database_manager.borrow_book(book_id, username)
            elif choice == "3":
                book_id = int(UserInterface.get_user_input("Enter the ID of the book you want to return: "))
                username = UserInterface.get_user_input("Enter your username: ")
                database_manager.return_book(book_id, username)
            elif choice == "4":
                username = UserInterface.get_user_input("Enter your username: ")
                database_manager.view_borrowed_books(username)
            elif choice == "5":
                username = UserInterface.get_user_input("Enter your username: ")
                database_manager.view_customer_account(username)
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


    @staticmethod
    def display_main_menu_librarian():
        print("Librarian Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

    @staticmethod
    def handle_librarian_main_menu(database_manager):
        while True:
            UserInterface.display_main_menu_librarian()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                UserInterface.handle_book_operations(database_manager)
            elif choice == "2":
                UserInterface.handle_user_operations(database_manager)
            elif choice == "3":
                UserInterface.handle_author_operations(database_manager)
            elif choice == "4":
                UserInterface.handle_genre_operations(database_manager)
            elif choice == "5":
                print("Exiting system...")
                break
            else:
                print("Invalid choice. Please try again.")

    # Book operations
    @staticmethod
    def display_book_menu():
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Modify book information")
        print("3. Remove a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Return to Main Menu")

    @staticmethod
    def handle_book_operations(database_manager):
        while True:
            UserInterface.display_book_menu()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                title = UserInterface.get_user_input("Enter the title of the book: ")
                author_name = UserInterface.get_user_input("Enter the author's name: ")
                genre_name = UserInterface.get_user_input("Enter the genre: ")
                publication_date = UserInterface.get_user_input("Enter the publication date (YYYY-MM-DD): ")
                
                author_id = database_manager.find_or_add_author(author_name)
                genre_id = database_manager.find_or_add_genre(genre_name)

                database_manager.add_new_book(title, author_id, genre_id, publication_date)
            elif choice == "2":
                book_title = UserInterface.get_user_input("Enter the title of the book to modify: ")
                books = database_manager.search_books_by_title(book_title)
                if not books:
                    print("No book found with that title. Returning to menu.")
                    continue
                elif len(books) > 1:
                    print("Multiple books found. Please specify by book ID:")
                    for book in books:
                        print(f"ID: {book[0]}, Title: {book[1]}")
                    book_id = int(UserInterface.get_user_input("Enter the book ID to modify: "))
                else:
                    book_id = books[0][0]
                
                new_title = UserInterface.get_user_input("Enter new title (press enter to skip): ")
                new_author_name = UserInterface.get_user_input("Enter new author's name (press enter to skip): ")
                new_genre_name = UserInterface.get_user_input("Enter new genre (press enter to skip): ")
                new_publication_date = UserInterface.get_user_input("Enter new publication date (YYYY-MM-DD, press enter to skip): ")

                author_id = database_manager.find_or_add_author(new_author_name) if new_author_name else None
                genre_id = database_manager.find_or_add_genre(new_genre_name) if new_genre_name else None

                database_manager.update_book(book_id, new_title, author_id, genre_id, new_publication_date)
                print("Book updated successfully.")
            elif choice == "3":
                book_id = int(UserInterface.get_user_input("Enter book ID to remove: "))
                database_manager.remove_book(book_id)
            elif choice == "4":
                keyword = UserInterface.get_user_input("Enter search keyword: ")
                database_manager.search_books(keyword)
            elif choice == "5":
                database_manager.display_all_books()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")


    # User operations
    @staticmethod
    def display_user_menu():
        print("User Operations:")
        print("1. Add a new user")
        print("2. Modify user information")
        print("3. Remove a user")
        print("4. Display all users")
        print("5. Return to Main Menu")

    @staticmethod
    def handle_user_operations(database_manager):
        while True:
            UserInterface.display_user_menu()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                name = UserInterface.get_user_input("Enter the user's name: ")
                email = UserInterface.get_user_input("Enter the user's email: ")
                phone = UserInterface.get_user_input("Enter the user's phone number: ")
                address = UserInterface.get_user_input("Enter the user's address: ")
                password = UserInterface.get_user_input("Enter the user's password: ")
                database_manager.add_new_user(name, email, phone, address, password)
            elif choice == "2":
                user_id = int(UserInterface.get_user_input("Enter user ID to modify: "))
                name = UserInterface.get_user_input("Enter new name (press enter to skip): ")
                email = UserInterface.get_user_input("Enter new email (press enter to skip): ")
                phone = UserInterface.get_user_input("Enter new phone number (press enter to skip): ")
                address = UserInterface.get_user_input("Enter new address (press enter to skip): ")
                password = UserInterface.get_user_input("Enter new password (press enter to skip): ")
                database_manager.update_user(user_id, name, email, phone, address, password)
            elif choice == "3":
                user_id = int(UserInterface.get_user_input("Enter user ID to remove: "))
                database_manager.remove_user(user_id)
            elif choice == "4":
                database_manager.display_all_users()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    # Author operations
    @staticmethod
    def display_author_menu():
        print("Author Operations:")
        print("1. Add a new author")
        print("2. Modify author information")
        print("3. Remove an author")
        print("4. Display all authors")
        print("5. Return to Main Menu")

    @staticmethod
    def handle_author_operations(database_manager):
        while True:
            UserInterface.display_author_menu()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                name = UserInterface.get_user_input("Enter author's name: ")
                biography = UserInterface.get_user_input("Enter author's biography (press enter to skip): ")
                database_manager.add_new_author(name, biography.strip() or None)
            elif choice == "2":
                author_id = int(UserInterface.get_user_input("Enter author ID to modify: "))
                name = UserInterface.get_user_input("Enter new name (press enter to skip): ")
                biography = UserInterface.get_user_input("Enter new biography (press enter to skip): ")
                database_manager.update_author(author_id, name, biography)
            elif choice == "3":
                author_id = int(UserInterface.get_user_input("Enter author ID to remove: "))
                database_manager.remove_author(author_id)
            elif choice == "4":
                database_manager.display_all_authors()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    # Genre operations
    @staticmethod
    def display_genre_menu():
        print("Genre Operations:")
        print("1. Add a new genre")
        print("2. Modify genre information")
        print("3. Remove a genre")
        print("4. Display all genres")
        print("5. Return to Main Menu")

    @staticmethod
    def handle_genre_operations(database_manager):
        while True:
            UserInterface.display_genre_menu()
            choice = UserInterface.get_user_input("Enter your choice: ")
            if choice == "1":
                name = UserInterface.get_user_input("Enter genre name: ")
                description = UserInterface.get_user_input("Enter genre description: ")
                database_manager.add_new_genre(name, description)
            elif choice == "2":
                genre_id = int(UserInterface.get_user_input("Enter genre ID to modify: "))
                name = UserInterface.get_user_input("Enter new name (press enter to skip): ").strip()
                description = UserInterface.get_user_input("Enter new description (press enter to skip): ").strip()
                database_manager.update_genre(genre_id, name, description)
            elif choice == "3":
                genre_id = int(UserInterface.get_user_input("Enter genre ID to remove: "))
                database_manager.remove_genre(genre_id)
            elif choice == "4":
                database_manager.display_all_genres()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
