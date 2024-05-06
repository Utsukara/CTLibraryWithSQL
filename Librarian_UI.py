import Book
import User
import Author
import Genre


def Librarian_Interface():
    print("Librarian Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Book_Operations()
    elif choice == "2":
        User_Operations()
    elif choice == "3":
        Author_Operations()
    elif choice == "4":
        Genre_Operations()
    elif choice == "5":
        print("Thank you for using the Library Management System!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        Librarian_Interface()



def Book_Operations():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. View book details")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Enter your choice: ")
    if choice == "1":
        Book.Add_New_Book()
    elif choice == "2":
        Book.Remove_Book()
    elif choice == "3":
        Book.View_Book_Details()
    elif choice == "4":
        Book.Search_Books()
    elif choice == "5":
        Book.Display_All_Books()
    else:
        print("Invalid choice. Please try again.")
        Book_Operations()



def User_Operations():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Enter your choice: ")
    if choice == "1":
        User.Add_New_User()
    elif choice == "2":
        User.View_User_Details()
    elif choice == "3":
        User.Display_All_Users()
    else:
        print("Invalid choice. Please try again.")
        User_Operations()



def Author_Operations():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Enter your choice: ")
    if choice == "1":
        Author.Add_New_Author()
    elif choice == "2":
        Author.View_Author_Details()
    elif choice == "3":
        Author.Display_All_Authors()
    else:
        print("Invalid choice. Please try again.")
        Author_Operations()



def Genre_Operations():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    choice = input("Enter your choice: ")
    if choice == "1":
        Genre.Add_New_Genre()
    elif choice == "2":
        Genre.View_Genre_Details()
    elif choice == "3":
        Genre.Display_All_Genres()
    else:
        print("Invalid choice. Please try again.")
        Genre_Operations()