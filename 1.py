
import    csv
db = []
with open('database/receptionists.csv', 'r') as cs :
    data = csv.reader(cs)
    for i in data:
        # pass the headers of csv
        if i == ['stid', 'username', 'password'] or i == ['username', 'password'] :
            continue
        # if list is True (mean if list is not empty)
        elif i :
            # append all userpass in list
            db.append(i)
    
    u = 'kal'
    p = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
    login = False
    # extract all lists from list
    for i in db :
        # check username on i[0] and password on i[1]
        if i[0] == u and i[1] == p :
            login = True
            print('granted')
        else :
            continue
    if login == False :
        print('Your username or passwrd is incorrect !')


