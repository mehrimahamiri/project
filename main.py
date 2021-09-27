from HandleFile import HandleFile
from colorama import Fore, Style, init  # منابع کمتر مصرف میشع چیزایی که احتیاج داریم امپورت میشه
import hashlib
from csv import writer, reader
from os import path, system
from prettytable import PrettyTable

init()


class Uni(object):
    login = False  # ta zamani ke login nakone false

    def __init__(self):
        print(Fore.RED + 'For start please use menu' + Style.RESET_ALL)

    def menu(self):
        # check Student_number.csv is exists or not --> if is not create the file 
        # self._check_file_exists('Student_number.csv' , '14000701') 
        while Uni.login == False:  # ta vaqti login nashode menue reset she

            print(
                Fore.CYAN + "\n\nـــــــــــــــــــــ Welcome to SELECT_UNIT  Demo ـــــــــــــــــــــ" + Style.RESET_ALL)

            choice = input("""
1: sign up
2: sign in
3: Quit

Please enter your choice: """)
            system("cls")
            # get choice and lead to attribute
            if choice == "1":
                # get student or receptionist then direct user to sign up
                self.get_char('signup')
            elif choice == "2":
                # get student or receptionist then direct user to sign up
                self.get_char('signin')
            elif choice == "3":
                exit()
            else:
                print(Fore.RED + "You must only select specified NUMBER")
                print(Fore.RED + "Please try again !" + Style.RESET_ALL)

    def get_char(self, sign_in_or_sign_up):
        '''
        get the registrant character
        '''
        while True:
            # system("cls")
            print(Fore.CYAN + "\n\nــــــــــــــــــــــــ  SELECT_TYPE  ــــــــــــــــــــــــ" + Style.RESET_ALL)

            choice = input("""
1: Student
2: Receptionist 
3: Quit
Please enter your choice: """)

            if choice == "1":
                char = 'Student'
                break

            elif choice == "2":
                char = 'Receptionist'
                break

            elif choice == "3":
                exit()

            else:
                system('cls')
                print(
                    Fore.RED + "           You must only select specified NUMBER         ")
                print(
                    Fore.RED + "                    Please try again !            " + Style.RESET_ALL)

        # go to the sign in or sign up depend on choose on the menu
        # char dadim ke bedonim ba kodom char mikhad vared she/baki tarafim
        if sign_in_or_sign_up == 'signup':
            self.sign_up(char)
        elif sign_in_or_sign_up == 'signin':
            self.sign_in(char)

    def sign_up(self, char):
        while True:
            username = input("\n\nPlease enter username: ")
            if username:
                break

        while True:
            # get information from user

            while True:
                password = input("Please enter password: ")
                if password:
                    break

            repeat_password = input("Please enter repat pasword: ")

            # information checker
            if password == repeat_password:
                # encoded the password
                encoded_pass = hashlib.sha256(password.encode()).hexdigest()

                if char == 'Student':
                    # give unique student id to student
                    last_stid = self._read_last_studentid()  # akhrin id
                    file = HandleFile('database/students.csv')
                    data = {'stid': last_stid, 'username': username,
                            'password': encoded_pass}  # meqdar dadim
                    system("cls")
                    print(Fore.GREEN + "\n\t\tYour account was created successfully!!" + Style.RESET_ALL)
                    print(
                        Fore.MAGENTA + f"\n\t\t=========================================\n\t\t\t  Your Student ID: {last_stid}\n\t\t\t  Status: Student\n\t\t\t  Uesrname: {username}\n\t\t\t  Password: {len(password) * '*'}\n\t\t=========================================" + Style.RESET_ALL)
                    # write last student id + 1
                    self._write_studentid(int(last_stid) + 1)

                elif char == 'Receptionist':
                    file = HandleFile('database/receptionists.csv')
                    data = {'username': username, 'password': encoded_pass}
                    system("cls")
                    print(Fore.GREEN + "\n\t\tYour account was created successfully!!" + Style.RESET_ALL)
                    print(
                        Fore.MAGENTA + f"\n\t\t=========================================\n\t\t\t  Status: Reception\n\t\t\t  Uesrname: {username}\n\t\t\t  Password: {len(password) * '*'}\n\t\t=========================================" + Style.RESET_ALL)

                file.append_info(data)  # append nahayi

                break

            else:
                print(
                    Fore.RED + "your password doesn't match with your Repeat password Please Try again !!" + Style.RESET_ALL)
                continue

    def _read_last_studentid(self):
        with open('student_number.txt', 'r') as id_file:
            return id_file.read()  # read and return

    def _write_studentid(self, last_studentid):
        with open('student_number.txt', 'w') as id_file:
            id_file.write(str(last_studentid))  # save akhrish chon W baqiye ro pak mikoen

    # def change_stid(self, number):
    #     with open('Student_number.csv', 'w') as cs:
    #         writer(cs).writerow([str(number)])
    #         print(f'The student id has been changed to {number} !')

    # rest data base

    # def reset_db(self):
    #     '''
    #     run and choose the db for reset the database
    #     '''
    #     while True:
    #         print(Fore.CYAN+"ـــــــــــــــــــــ Welcome to database reset ـــــــــــــــــــــــ"+Style.RESET_ALL)
    #         choice = input("""
    #         1: Student db
    #         2: Receptionist db
    #         3: Quit
    #         Please enter your choice: """)

    #         if choice == "1":
    #             with open('database/students.csv', 'w') as cs:
    #                 writer(cs).writerow([])
    #                 print('The database has been reseted !!')
    #                 break
    #         elif choice == "2":
    #             with open('database/receptionists.csv', 'w') as cs:
    #                 writer(cs).writerow([])
    #                 print('The database has been reseted !!')
    #                 break
    #         elif choice == '3':
    #             exit()
    #         else:
    #             print(
    #                 "__________________________________________________________________")
    #             print(
    #                 Fore.RED+"                       You must only select specified NUMBER         ")
    #             print(
    #                 Fore.RED+"                            Please try again !            "+Style.RESET_ALL)
    #             print(
    #                 "__________________________________________________________________")

    # def _check_file_exists(self,filename , stid_number):
    #     stats = path.isfile(filename)
    #     if stats == False:
    #         self.change_stid(stid_number)

    def sign_in(self, char):
        while True:
            username = input('\n\nEnter your username: ')
            password = input('Enter your password: ')
            encoded_pass = hashlib.sha256(password.encode()).hexdigest()
            users = HandleFile("database\students.csv").read_info()
            user = _pass = False
            for u in users:
                if username == u[1]:
                    user = True
                    if encoded_pass == u[2]:
                        _pass = True
                        break
            if user and _pass:
                break
            elif not user:
                print(Fore.RED + 'User not found.' + Style.RESET_ALL); continue
            elif not _pass:
                print(Fore.RED + 'Password is incorrect!' + Style.RESET_ALL); continue
        system("cls")

        login_msg = Fore.YELLOW + f" {char} ____________________ {username} _______________________  Logged in!" + Style.RESET_ALL

        if char.lower() == 'student':

            table = PrettyTable()
            table.field_names = ['Course', 'Capacity', 'Remaining']  # titel list

            while True:

                system("cls")
                print(login_msg)  # sarbarg
                user_select = input(
                    "\n\n1- Course list\n2- Course search\n3- View all units\n4- Exit\n\nPlease enter your choice: ")

                if not user_select.isdigit() or len(user_select) != 1:
                    print(Fore.RED + "\nYour choice is incorrect, Please try again!" + Style.RESET_ALL)
                    continue

                user_select = int(user_select)

                if user_select == 1:

                    myFile = HandleFile(r'database/courses.csv')
                    data = myFile.read_info()

                    for d in data:
                        table.add_row([d[0], d[1], d[2]])

                    print(table)
                    system("pause")  # dastor cmd ejramishe

                elif user_select == 2:

                    def my_func(lst):
                        lst[0] = lst[0].lower()
                        return lst

                    data = list(map(my_func,
                                    filter(lambda d: len(d) > 0, HandleFile('./database/courses.csv').read_info()[1:])))
                    courses = [d[0] for d in data]

                    table = PrettyTable()
                    table.field_names = ['Course', 'Capacity', 'Remaining']

                    while True:

                        course_name = input('\nEnter a course name (q for Quit): ')

                        system("cls")
                        print(login_msg)

                        if course_name == 'q':
                            break

                        elif not course_name or course_name not in courses:
                            print(Fore.RED + "\nCourse name not exist! Try again. -> (q for Quit)" + Style.RESET_ALL)
                            continue

                        for d in data:

                            if d[0] == course_name:
                                table.add_row([d[0].title(), d[1], d[2]])

                        print(table)
                        table.clear_rows()

                elif user_select == 4:

                    break

        elif char.lower() == 'receptionist':

            table = PrettyTable()
            table.field_names = ['Course', 'Capacity', 'Remaining', 'Unit', 'Teacher']


            while True:
                system("cls")
                print(login_msg)

                user_select = input(
                    "\n\n1- Course list\n2- Course search\n3- View all units\n4- Add course\n5- Exit\n\nPlease enter your choice: ")

                if not user_select.isdigit() or len(user_select) != 1:
                    print(Fore.RED + "\nYour choice is incorrect, Please try again!" + Style.RESET_ALL)
                    continue

                user_select = int(user_select)

                if user_select == 1:

                    myFile = HandleFile(r'database/courses.csv')
                    data = myFile.read_info()

                    for d in data:
                        table.add_row([d[0], d[1], d[2], d[3], d[4]])

                    print(table)
                    system("pause")

                elif user_select == 2:

                    data = HandleFile('./database/courses.csv').read_info()
                    courses = [d[0] for d in data]

                    while True:

                        course_name = input('\nEnter a course name (q for Quit): ')

                        system("cls")
                        print(login_msg)

                        if course_name == 'q':
                            break

                        elif not course_name or course_name not in courses:
                            print(
                                Fore.RED + "\nCourse name not exist! Try again. -> (q for Quit)" + Style.RESET_ALL); continue

                        for d in data:

                            if d[0] == course_name:
                                table.add_row([d[0], d[1], d[2], d[3], d[4]])

                        print(table)
                        table.clear_rows()

                elif user_select == 4:
                    data = {
                        'course': None,
                        'capacity': None,
                        'remaining': None,
                        'unit': None,
                        'teacher': None
                    }
                    d = iter(data)  # vorodi ro qabel harkat mikone done done gz index0 ta ...
                    k = next(d)  # done done mire element badi  mesle for valo dasti

                    print(Fore.RED + "\nSend 'q' to Cancel adding." + Style.RESET_ALL)

                    status = ''

                    while True:  # chek darse tekrar

                        if not k: break  # age residi be akhrin vorodi ke bayad begire break kon
                        usr_input = input(f'\r\nEnter {k}: ')  # ro kilid balai hharkat kon va meqdar begir

                        if not usr_input:
                            system("CLS")
                            print(login_msg)
                            print(Fore.RED + "\nSend 'q' to Cancel adding." + Style.RESET_ALL)
                            continue

                        if usr_input.lower() == 'q':
                            status = 'quit'
                            break

                        data[k] = usr_input
                        if k == 'course':
                            courses = map(lambda e: e[0].lower(), filter(lambda x: len(x) > 0, HandleFile(
                                r"./database/courses.csv").read_info()))
                            if data[k].lower() in courses:
                                print("\nCourse name duplicate!")
                                continue
                        k = next(d, '')  # key dic ke ba estefade ba estefade az tabe iter to key ha harekat mikone

                    print(status)
                    if status == 'quit':
                        continue

                    # data = {
                    #     'course': None,
                    #     'capacity': None,
                    #     'remaining': None,
                    #     'unit': None,
                    #     'teacher': None
                    # }
                    # d = iter(data)  # vorodi ro qabel harkat mikone done done gz index0 ta ...
                    # while True:  # chek darse tekrar
                    #     k = next(d, '')  # done done mire element badi  mesle for valo dasti
                    #
                    #     if not k:
                    #         break  # age residi be akhrin vorodi ke bayad begire break kon
                    #
                    #     while True:
                    #         inp = input(f'Enter {k}: ')
                    #         if inp:
                    #             break
                    #         else:
                    #             system('cls')
                    #             print(login_msg)
                    #             continue
                    #
                    #     data[k] = inp  # ro kilid balai hharkat kon va meqdar begir
                    #     if k == 'course':
                    #         courses = list(map(lambda e: e[0], HandleFile(r"./database/courses.csv").read_info()))
                    #
                    #         if not data[k]:
                    #             continue
                    #
                    #         elif data[k] in courses:
                    #             print("Course name duplicate!")
                    #             continue
                    #     k = next(d, '')  # key dic ke ba estefade ba estefade az tabe iter to key ha harekat mikone
                    result = self.add_course(
                        data['course'],
                        data['capacity'],
                        data['remaining'],
                        data['unit'],
                        data['teacher']
                    )

                    if result:

                        print(
                            Fore.GREEN + f"\n\n{data.get('course')} Successfully added to your courses!" + Style.RESET_ALL)
                        system('pause')
                        continue
                    else:

                        print(Fore.RED + "Oh sorry :( We have problem" + Style.RESET_ALL)

                    break

                elif user_select == 5:

                    break

            # table.clear_rows()

        # print(user_select)

        db = []

        # get all users and passwords
        with open(f'database/{char}s.csv', 'r') as cs:
            data = reader(cs)
            for i in data:
                # pass the headers of csv
                if i == ['stid', 'username', 'password'] or i == ['username', 'password']:
                    continue
                # if list is True (mean if list is not empty)
                elif i:
                    # append all userpass in list
                    db.append(i)
            # extract all lists from list
            # print('user:',username , 'password:', encoded_pass)
            for i in db:  # [1400,amofogh,a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3]
                if char == 'Student':
                    # check username on i[1] and password on i[2]
                    if i[1] == username and i[2] == encoded_pass:
                        Uni.login = True

                elif char == 'Receptionist':  # [qwe,a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3]
                    # check username on i[0] and password on i[1]
                    if i[0] == username and i[1] == encoded_pass:
                        Uni.login = True

            if Uni.login == False:
                print('Your username or passwrd is incorrect !')
                # after user authorised change login to True

            elif Uni.login == True:
                pass

    def add_course(self, course, capacity, remain, unit, teacher):

        course_data = {

            'course': course,
            'capacity': int(capacity),
            'remaining': remain,
            'unit': unit,
            'teacher': teacher

        }

        file = HandleFile('database/courses.csv')

        try:
            file.append_info(course_data)

        except Exception as error:

            print(error)
            return False

        # print(f'The {course} with {capacity} credits has added to the database !')
        return True

    def delete_course(self, course_name):
        '''
        get all courses from csv then write all courses except course name user want to delete
        '''
        courses = self.read_all_courses()

        # take course name user want to get out  of the list
        for index, list_ in enumerate(courses):
            if list_[0] == course_name:
                courses.pop(index)

        with open('database/courses.csv', 'w') as file:
            # empty the courses.csv with 'w' mode then write with add_course()
            for j in courses:
                self.add_course(j[0], j[1])

    def read_all_courses(self):
        courses = []
        with open('database/courses.csv', 'r') as cs:
            # read csv file
            res = reader(cs)
            # get data from the list
            for i in res:
                # skip the header
                if i == ['course_name', 'credits']:
                    continue
                if i:
                    # add another course to the list
                    courses.append(i)
        return courses

    def search(self, course):
        with open('database/courses.csv', 'r') as cs:
            # read csv file
            res = reader(cs)
            # get data from the list
            for i in res:
                # skip the header
                if i == ['course_name', 'credits']:
                    continue
                if i:
                    # search the lesson
                    if i[0] == course:
                        return i


instanse = Uni()
# instanse.change_stid(1500)
# instanse.change_stid(1400)
# instanse.reset_db()
instanse.menu()
# instanse.add_course('php' , 4)
# instanse.add_course('django' , 5)
# instanse.add_course('python' , 1)
# instanse.delete_course('php')

# class Student(Uni):
#     all_credits = 40
#     passed_credits = 0

#     def __init__(self):

#         if super().login != True:
#             super().menu()
#         #edit: print khoshgel bezar (menu of student)

#     def logout(self):
#         Uni.login = False
#         super().menu()

#     def courses_list(self):
#         courses = super().read_all_courses()
#         # edit: print khoshgel bezar
#         print('courses:' , courses )
#         print('all credits:' , Student.all_credits )
#         remain_credits = Student.all_credits - Student.passed_credits
#         print('remain credits:' , remain_credits)

#     def search_course(self,course):
#         res = super().search(course)
#         #edit: print khoshgel bezar
#         # print('course :' , res[0] , 'credits : ' , res[1])

# stdn = Student()
# stdn.search_course('django')
