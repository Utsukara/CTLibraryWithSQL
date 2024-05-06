from user_interface import UserInterface
from database import DatabaseManager

def main():
    db_manager = DatabaseManager(host='localhost', database='library', user='root', password='password')
    db_manager.connect()

    while True:
        UserInterface.display_main_menu()
        choice = UserInterface.get_user_input("Enter your choice: ")
        if choice == "1":
            UserInterface.handle_book_operations(db_manager)
        elif choice == "2":
            # Similar setup for user operations
            pass
        elif choice == "3":
            # Similar setup for author operations
            pass
        elif choice == "4":
            # Similar setup for genre operations
            pass
        elif choice == "5":
            print("Exiting system...")
            db_manager.disconnect()
            exit()
        else:
            print("Invalid choice. Please try again.")

    db_manager.disconnect()

if __name__ == "__main__":
    main()