
from customer import *
from bank import *
import random
def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username already exists")
        SignUp()
    else:
        print("Username is avialable please proceed")
        password = input("Enter your password: ")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers where account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break

    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
           password = input(f"Welcome {username.capitalize()} Enter Password: ")
           temp = db_query(f"SELECT password FROM customers where username = '{username}';")
           #print(temp[0][0])
           if temp[0][0] == password:
               print("Sign IN Succesfully")
               return username
           else:
               print("Wrong Password Try Again")
               continue
    else:
        print("Enter correct Username")
        SignIn()