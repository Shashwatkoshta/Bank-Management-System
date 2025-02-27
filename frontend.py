
import streamlit as st
from database import db_query, mydb
from customer import Customer
from bank import Bank
import random

# Function to handle user signup
def sign_up():
    st.subheader("Sign Up")
    username = st.text_input("Create Username")
    password = st.text_input("Enter Password", type="password")
    name = st.text_input("Enter Your Name")
    age = st.number_input("Enter Your Age", min_value=18, max_value=100, step=1)
    city = st.text_input("Enter Your City")

    if st.button("Register"):
        temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
        if temp:
            st.error("Username already exists! Try a different one.")
        else:
            account_number = random.randint(10000000, 99999999)
            db_query(f"INSERT INTO customers VALUES ('{username}', '{password}', '{name}', {age}, '{city}', 0, {account_number}, 1);")
            mydb.commit()
            bobj = Bank(username, account_number)
            bobj.create_transaction_table()
            st.success(f"Account created successfully! Your account number is {account_number}")

# Function to handle user login
def sign_in():
    st.subheader("Sign In")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
        if temp and temp[0][0] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password!")

# Function to perform banking operations
def banking_services():
    username = st.session_state["username"]
    account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{username}';")[0][0]
    bobj = Bank(username, account_number)

    st.subheader(f"Welcome, {username}")

    option = st.radio("Choose Banking Service", ["Balance Enquiry", "Deposit", "Withdraw", "Fund Transfer"])

    if option == "Balance Enquiry":
        if st.button("Check Balance"):
            balance = db_query(f"SELECT balance FROM customers WHERE username = '{username}';")[0][0]
            st.success(f"Your balance is ₹{balance}")

    elif option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=1, step=1)
        if st.button("Deposit"):
            bobj.deposit(amount)
            mydb.commit()
            st.success(f"₹{amount} deposited successfully!")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=1, step=1)
        if st.button("Withdraw"):
            bobj.withdraw(amount)
            mydb.commit()
            st.success(f"₹{amount} withdrawn successfully!")

    elif option == "Fund Transfer":
        recipient_acc = st.text_input("Enter Receiver's Account Number")
        amount = st.number_input("Enter amount to transfer", min_value=1, step=1)
        if st.button("Transfer"):
            bobj.fundtransfer(recipient_acc, amount)
            mydb.commit()
            st.success(f"₹{amount} transferred successfully!")

    # Logout Button
    if st.button("Log Out"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.experimental_rerun()

# Streamlit UI Logic
st.title("Shashwat Bank")
st.sidebar.title("Navigation")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    option = st.sidebar.radio("Choose an option", ["Sign Up", "Sign In"])
    if option == "Sign Up":
        sign_up()
    else:
        sign_in()
else:
    banking_services()
