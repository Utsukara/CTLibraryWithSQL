from user_interface import UserInterface
from database import DatabaseManager

def main():
    # Initialize the DatabaseManager with your database credentials
    db_manager = DatabaseManager(host='localhost', database='library', user='root', password='Kellyisnothelping24*')
    
    # Display the main menu and handle user input
    UserInterface.handle_main_menu(db_manager)

if __name__ == "__main__":
    main()