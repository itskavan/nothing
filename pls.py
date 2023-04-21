usernames = ["user1", "user2"]
passwords = ["12345678","00000000"]
loggedin = True

while loggedin == True:
    username = input("please enter username : ")
    if username not in usernames:
        print("try again or create new username(enter 1 to try again , enter 2 to create new username)")
        c = int(input())
        if c == 2:
                newusr = input("enter new username... ")
                usernames.append(newusr)
    else:
        password = input("please enter password : ")
        if password in passwords:
            print("successfully logged in")
            loggedin = False
        else:
            print("try again or create new password (enter 1 to try again , enter 2 to create new password)")
            c = int(input())
            if c == 2:
                newpass = input("enter new password... ")
                passwords.append(newpass)
