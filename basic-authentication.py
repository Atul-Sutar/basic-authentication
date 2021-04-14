#user authentication
password = "secret"
check = False
username = 'user'
atm = 2

while not check:
    u_user = input("enter username : ")
    p_pass = input("enter password : ")
    if (username == u_user)and(password == p_pass)and(atm != 0):
        print("Access Granted")
        break
    else:
        if atm:
            print("Access Denied")
            print("your credentials are wrong. try gain")
            atm -= 1
        else:
            print("you have exhausted your attempt.")
            print("try rnning program again.")
            break
"""created by Atul"""
