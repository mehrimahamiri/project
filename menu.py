#import csv
import sys

def main():
    menu()

def menu():
    print("ـــــــــــــ Welcome to SELECT_UNIT  Demo ـــــــــــــــ")
    print()

    choice = input("""
    1: Login
    2: Logout

    Please enter your choice: """)

    if choice == "1" :
        login()
    elif choice=="2":
        quit()
    else:
        print("You must only select NUMBER")
        print("Please try again !")
        menu()

def login():
    choice = input("""
    1: Student
    2: Receptionist 
    3: EXIT
    Please enter your choice: """)
    
    if choice == "1" :
        student()
    elif choice=="2":
        Receptionist()
    elif choice == "3":
        quit()
    else:
        print("You must only select NUMBER")
        print("Please try again !")
        login()

def student():
    pass

def Receptionist():
    pass

#the program is initiated, so to speak, here
main()