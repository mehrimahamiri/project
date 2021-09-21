import platform
import getpass
import time
import os

while True :
    user_name = input("plz enter username: ")
    password = getpass.getpass("plz enter password: ")
    confirm_password = getpass.getpass("plz enter repat pasword: ")

    if password == confirm_password:
        print("Done.")
        break
    else:
        print("Your password doesn't match with your confirm password.")
        print("Enter the password and confirm password again.")
        
        time.sleep(2)

        if platform.system().lower() == "windows":
            os.system("cls")
        elif platform.system().lower() == "linux":
            os.system("clear")
        else:
            os.system("clear")

        pass