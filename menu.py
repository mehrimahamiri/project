def main():
    menu()

def menu():
    print("\nـــــــــــــ Welcome to SELECT_UNIT  Demo ـــــــــــــــ\n")

    choice = int(input("""
    1: Login
    2: Logout

    Please enter your choice: """))

    if choice == 1:
        login()
    elif choice == 2:
        print("Ok, Bye!")
        quit()
    else:
        print("You must only select NUMBER")
        print("Please try again!")

        menu()

def login():
    choice = int(input("""
    1: Student
    2: Receptionist 
    3: EXIT
    Please enter your choice: """))
    
    if choice == 1 :
        student()
    elif choice == 2:
        Receptionist()
    elif choice == 3:
        print("Ok, Bye!")
        quit()
    else:
        print("You must only select NUMBER")
        print("Please try again!")
        login()

def student():
    pass

def Receptionist():
    pass

#the program is initiated, so to speak, here
main()