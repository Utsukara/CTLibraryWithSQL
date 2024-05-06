import User_UI
import Librarian_UI

#User/Librarian Selection

def Librarian_User_Selection():
    print("Welcome to the Library Management System!")
    print("Are you a User or a Librarian?")
    print("1. User")
    print("2. Librarian")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        User_UI.User_Interface()
    elif choice == "2":
        Librarian_UI.Librarian_Interface()
    elif choice == "3":
        print("Thank you for using the Library Management System!")
    else:
        print("Invalid choice. Please try again.")
        Librarian_User_Selection()