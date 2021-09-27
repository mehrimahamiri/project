#import csv
import hashlib
import HandleFile
from colorama import init
from colorama import Fore,Style

class Uni :
    count=1400
    def __init__(self):
        Uni.count+=1
        while True :
            self.menu()

    def menu(self):
        init()
        print(Fore.BLUE+"ــــــــــــــــــــــــــ Welcome to SELECT_UNIT  Demo ــــــــــــــــــــــــــــ"+Style.RESET_ALL)
        print()

        choice = input("""
        1: sign up
        2: sign in
        3: Quit

        Please enter your choice: """)

        if choice == "1" :
            self.sign_up()
        elif choice == "2" :  
            self.sign_in()
        elif choice=="3":
                exit()
        else:
            print()
            init()
            print(Fore.RED+"You must only select specified NUMBER" )
            print(Fore.RED+"Please try again !"+Style.RESET_ALL)
            
    def sign_up(self):
        while True :
            choice = input("""
            1: Student
            2: Receptionist 
            3: EXIT
            Please enter your choice: """)
            
            if choice == "1" :
                stats = 'student'
                self._save_in_csv(stats)
                break
            
            elif choice=="2":
                stats = 'Receptionist'
                self._save_in_csv(stats)
                break
            
            elif choice == "3":
                    exit()
                    
            else:
                print("__________________________________________________________________")
                init()
                print(Fore.RED+"                       You must only select specified NUMBER         " )
                print(Fore.RED+"                            Please try again !            "+Style.RESET_ALL)
                print("__________________________________________________________________")
            
    def _save_in_csv(self , stats):
        user_name=input("please enter username :")
        password=input("please enter password :")
        repeatpass=input("please enter repat pasword :")
        while True :
            if password==repeatpass :
                pas = hashlib.sha256(password.encode()).hexdigest()
                file = HandleFile.handleFile('hashing.csv')
                stdn = {Uni.count , user_name ,stats ,pas }
                file.append_info_user(stdn)
                print("sign up !!")
                print(f"your ID : {Uni.count} stats:{ stats} Uesrname : {user_name} password :{len(password)*'*'}")
                break
            else :
                print("your password doesn't match with your repeatpassword, enter the password and repeatpass again")
                password=input("plz enter password :")
                repeatpass=input("plz enter repat pasword :")
    def Receptionist(self):
        pass
    def sign_in(self):
        pass
        

uni1=Uni()
