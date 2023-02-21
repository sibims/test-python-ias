from user.sign import SignIn
from user.sign import SignUp
from user.sign import View


class welcome:

    flag = True
    count = 0

    while flag:
        print("-"*138)
        print(" "*50, "_-"*3, "Welcome to Aspire Systems", "-_"*3)
        print("")
        print("-"*138)
        choice = 7
        try:
            choice = int(input(
                "You are able to\n1. Sign Up\n2. Sign In\n3. View Accounts\n4. Exit\n0. Terms and Conditions\n\nEnter your choice: "))
        except:
            print("Keyboard Interrupt Raised. Return to Home")
            flag = True
        match choice:
            case 1:
                SignUp().add()
                flag = True
            case 2:
                SignIn().login()
                flag = True
            case 3:
                View().viewacc()
                flag = True
            case 4:
                exit()
            case 0:
                print()
                fp = open(r"t&c.txt", "r")
                print(fp.read())
                fp.close()
            case _:
                print("Invalid choice")
                flag = True
