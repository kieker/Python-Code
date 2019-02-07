from bankaccount import BankAcc
from gui import Gui
import mysql.connector
import tkinter as tk
#import scrypt

mydb = mysql.connector.connect(
    host="sql1.jnb3.host-h.net",
    user="kieketehht_4",
    passwd="uVv4MZ4rER6NEfAaKtb8",
    database="kieketehht_pyt"
)

def main():

    try:
        mycursor = mydb.cursor()
        mycursor.execute("USE kieketehht_pyt")
        mycursor.execute("SHOW TABLES")
        results  = mycursor.fetchall()
        print("All Tables currently in Database: ", results)

        results_list = [item[0] for item in results]
        if "users" not in results_list:
            mycursor.execute("CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),password VARCHAR(255), account_no VARCHAR(200), amount FLOAT)")
            print("Users table created")
        else:
            print("Users table already exist. Moving on.")

    except Exception as ex:
       display_error_message(ex)

    win = Gui()
    win.main_gui()

def display_error_message(ex):
    errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
    message = errormessage.format(type(ex).__name__, ex.args)
    print("There was an issue with the program, please try again later")
    print(message)

def create_user(username,password,amount):
    account= BankAcc(username,password,amount,mydb)

main()
