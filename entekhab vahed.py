import termcolor
import platform
import getpass
import time
import art
import os

print(termcolor.colored(art.text2art("Welcome!"), "cyan"))

while True :
    user_name = input("plz enter username: ")
    password = getpass.getpass(termcolor.colored("plz enter password: ", "yellow"))
    confirm_password = getpass.getpass(termcolor.colored("plz enter repat pasword: ", "yellow"))

    if password == confirm_password:
        print(termcolor.colored("\nDone.", "green"))
        break
    else:
        print(termcolor.colored("\nYour password doesn't match with your confirm password.", "red"))
        print(termcolor.colored("Enter the password and confirm password again.", "red"))
        
        time.sleep(2)

        if platform.system().lower() == "windows":
            os.system("cls")
        elif platform.system().lower() == "linux":
            os.system("clear")
        else:
            os.system("clear")

        pass