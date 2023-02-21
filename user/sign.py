from library.session import Session
from datetime import datetime
from getpass import getpass
import time


class SignUp:
    _fname = []
    _lname = []
    _mobile = []
    _username = []
    _password = []
    _passcode = []

    def disclaimer(type):
        string = ["Don't Disclose your Passcode with anyone!",
                  "Don't Disclose your Credentials with anyone!"]
        for char in string[type]:
            print(char, end='', flush=True)
            time.sleep(.05)
        print()

    # add user
    def add(self):

        print("")
        print("_-"*3, "Sign Up", "-_"*3)
        print("")

        try:
            ftemp = input("Enter First Name: ")
            ltemp = input("Enter Last Name: ")
            mtemp = input("Enter Mobile Number: ")
            if len(ftemp) >= 4 and len(ltemp) >= 3 and len(mtemp) == 10:
                SignUp.disclaimer(type=0)
                SignUp._passcode.append(getpass("Enter a secret passcode: "))
                SignUp._fname.append(ftemp)
                SignUp._lname.append(ltemp)
                SignUp._mobile.append(mtemp)
                SignUp._username.append(
                    ftemp[0:4]+'.'+ltemp[0:3]+'@'+mtemp[6:9])
                SignUp._password.append(ftemp[0:4]+'.'+mtemp[6:10])
                print("\nAccount Created Successfully\n")
                for i in range(len(SignUp._fname)):
                    print(
                        f"First name: {SignUp._fname}, FTemp: {ftemp}, Last Name: {SignUp._lname}, LTemp: {ltemp}")
            else:
                print("Requirement Not Satisfied! Try again now.")
        except:
            print("Keyboard Interrupt raised. Returning to homepage.")
            return None

# show user


class View(SignUp):
    def viewacc(self):
        x = len(SignUp._fname)
        print()
        print("_-_", "List of Usernames", "_-_")
        for i in range(0, x):
            print(
                f"{SignUp._fname[i]}")
            print("")
            input("Press any key to continue...\n")
            print("-_"*3, "Sign In Credentials", "_-"*3)
            print("")
            try:
                choice = int(
                    input("You can \n1. View ID Password\n2. Sign In\n3. Back\nEnter Your Choice: "))
            except:
                print("Only numeric values are allowed!")
            match choice:
                case 1:
                    Credentials().username()
                    break
                case 2:
                    SignIn().login()
                case 3:
                    break
                case _:
                    print("Invalid Option!")
                    View().viewacc()

# create username and password


class Credentials(SignUp):
    def username(self):
        print()
        print("-_"*3, "View Credentials", "_-"*3)
        print()
        ftemp = input("Enter your First Name: ")
        ltemp = input("Enter your Last Name: ")
        mtemp = str(input("Enter your Mobile Number: "))
        ptemp = str(getpass("Enter your Passcode: "))
        for i in range(len(SignUp._fname)):
            if (ftemp == SignUp._fname[i]):
                if (ltemp == SignUp._lname[i]):
                    if (mtemp == SignUp._mobile[i]):
                        if (ptemp == SignUp._passcode[i]):
                            print("")
                            time.sleep(1)
                            SignUp.disclaimer(type=1)
                            print(
                                f"\nUserName: {SignUp._username[i]}, Password: {SignUp._password[i]}")
                            input("\nPress any key to continue....\n")
                        else:
                            print("Passcode Mismatch!")
                    else:
                        print("Mobile Number Mismatch")
                else:
                    print("Last Name Mismatch")
            else:
                print("First Name Mismatch")
        return None

# Sign In Class


class SignIn(SignUp):
    def login(self):
        print("")
        print("-_"*3, "SignIn", "_-"*3)
        print("")
        try:
            uname = input("Enter your Username: ")
            upass = getpass("Enter your Password: ")
            flag = True
        except:
            print("Keyboard Interrupt!")
            flag = False
        while flag:
            for i in range(len(SignUp._username)):
                if uname == SignUp._username[i]:
                    if upass == SignUp._password[i]:
                        print()
                        print("_-_", "\4SignIn Successful!\4", "_-_")
                        print()
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        print(f"Successful SignIn at: {current_time}\n")
                        choice = 0
                        try:
                            choice = int(input(
                                "You can view:\n1. Scheduled Sessions\n2. Attendance Percentage\n3. SignOut\nEnter your choice: "))
                        except:
                            print("Only numerical values are valid.")
                        match choice:
                            case 1:
                                Session.schedule(self, SignUp._fname[i])
                                flag = True
                            case 2:
                                Session.attendance(self, SignUp._fname[i])
                                flag = True
                            case 3:
                                View().viewacc()
                                flag = False
                            case _:
                                print("No option found")
                    else:
                        print("Password Mismatch")
                        return None
                else:
                    print("Username Mismatch")
                    return None
        print("Press any key to continue...\n")
        return None
