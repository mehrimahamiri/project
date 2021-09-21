import platform
import getpass
import time
import os

user_name=input("plz enter username :")
password=input("plz enter password :")
repeatpass=input("plz enter repat pasword :")
while True :
    if password==repeatpass :
        break
    else :
        print("your password doesn't match with your repeatpassword, enter the password and repeatpass again")
        password=input("plz enter password :")
        repeatpass=input("plz enter repat pasword :")