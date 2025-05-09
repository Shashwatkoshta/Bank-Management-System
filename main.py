from register import *
from bank import *
print("Welcome to Shashwat Banking project")
status = False

while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn"))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid input from Options")
    except ValueError:
        print("Invalid Input Try again with numbers")

account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")


while status:
    print(f"Welcome {user.capitalize()} Choose your banking service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"
                             ))
        if facility >= 1 and facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_number[0][0] )
                bobj.balanceenquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter amount to Deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid Input ie. Number")
                        continue
                
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter amount to Withdraw: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit() 
                        status = False
                    except ValueError:
                        print("Enter valid Input ie. Number")
                        continue
                      
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        status = False
                    except ValueError:
                        print("Enter valid Input ie. Number")
                        continue
                
        else:
            print("Please Enter Valid input from Options")
            continue
    except ValueError:
        print("Invalid Input Try again with numbers")