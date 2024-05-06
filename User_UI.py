

def User_Interface():
    print("User Main Menu:")
    print("1. Search Books")
    print("2. Check Out Book")
    print("3. Return Book")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Search_Books()
    elif choice == "2":
        Check_Out_Book()
    elif choice == "3":
        Return_Book()
    elif choice == "4":
        print("Thank you for using the Library Management System!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        User_Interface()


def Search_Books():
    pass

def Check_Out_Book():
    pass

def Return_Book():
    pass