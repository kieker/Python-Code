import uuid
import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host="sql1.jnb3.host-h.net",
    user="kieketehht_4",
    passwd="uVv4MZ4rER6NEfAaKtb8",
    database="kieketehht_pyt"
)

class BankAcc:
    def __init__(self, name, password, amount):
        try:
            self.acc_holder = name
            self.acc_num = str(uuid.uuid4())
            #self.acc_type = typeacc

            if amount:
                self.amount = amount
            else:
                self.amount = 0

            mycursor = mydb.cursor()
            check_user = "SELECT id FROM users WHERE name = '%s'" %(name.get())
            mycursor.execute(check_user)
            results = mycursor.fetchall()

            if len(results) > 0:
                user_exists = tk.Label(text="User already exists, please try again")
                user_exists.pack()
                self.id = results[0]
            else:
                if int(amount.get()) == 0:
                    amount = 0
                else:
                    amount = int(amount.get())

                command = "INSERT INTO users(name,password,amount) VALUES('%s','%s','%d')" % (name.get(), password.get(), amount)
                mycursor.execute(command)

                mydb.commit()

                self.id = mycursor.lastrowid

                user_created = tk.Label(text="Your user has been created with acc number: "+ str(self.acc_num))
                user_created.pack()
                # if user_exists in locals():
                   # user_exists.pack_forget()

        except Exception as ex:
            errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
            message = errormessage.format(type(ex).__name__, ex.args)
            print("There was an issue connecting to your database, please try again later")
            print(message)

    def withdraw(self, amount):

        mycursor = mydb.cursor()
        self.amount -= amount

        mycursor.execute("UPDATE amount WHERE id = '%d'") %(self.id)
        return self.amount

    def withdraw_render(self):
        heading = tk.Label(text="Withdraw money")
        heading.pack()

    def deposit(self, amount):
        self.amount += amount

    def account_ops(win):
        reset_window(win)
        heading = tk.Label(text="Account Operations")
        heading.pack()
        withdraw = tk.Button(text="Withdraw", command="withdraw_render")
        withdraw.pack()

        deposit = tk.Button(text="Withdraw", command="deposit_render")
        deposit.pack()


        print("Account operations:")
        print("1 - Withdraw")
        print("2 - Deposit ")
        print("3 - Back")