class UserInterface:
    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def display_main_menu():
        print("Welcome to the Library Management System!")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

    @staticmethod
    def handle_main_menu(database_manager):
        while True:
            UserInterface.display_main_menu()
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
                exit()
            else:
                print("Invalid choice. Please try again.")

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
                # Add new book code
                pass
            elif choice == "2":
                # Modify book information code
                pass
            elif choice == "3":
                # Remove a book code
                pass
            elif choice == "4":
                # Search for a book code
                pass
            elif choice == "5":
                # Display all books code
                pass
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

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
                # Add new user code
                pass
            elif choice == "2":
                # Modify user information code
                pass
            elif choice == "3":
                # Remove a user code
                pass
            elif choice == "4":
                # Display all users code
                pass
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

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
                # Add new author code
                pass
            elif choice == "2":
                # Modify author information code
                pass
            elif choice == "3":
                # Remove an author code
                pass
            elif choice == "4":
                # Display all authors code
                pass
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

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
                # Add new genre code
                pass
            elif choice == "2":
                # Modify genre information code
                pass
            elif choice == "3":
                # Remove a genre code
                pass
            elif choice == "4":
                # Display all genres code
                pass
            elif choice == "5":
                break            
            else:
                print("Invalid choice. Please try again.")