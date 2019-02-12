import uuid
import mysql.connector
from bcrypt import hashpw, gensalt


mydb = mysql.connector.connect(
    host="sql1.jnb3.host-h.net",
    user="kieketehht_4",
    passwd="uVv4MZ4rER6NEfAaKtb8",
    database="kieketehht_pyt"
)

class BankAcc:
    def __init__(self, name, password, amount = 0):

        self.password=password.get()
        try:
            self.acc_holder = name.get()
            self.acc_num = str(uuid.uuid4())
            self.amount = 0
            self.id = 0
            self.message = " "

            self.password = hashpw(self.password.encode('utf-8'), gensalt())

            #self.acc_type = typeacc

            if amount is not '' or amount is not None:
                try:
                    amount_nr = amount.get()
                    self.amount = int(amount_nr)

                except ValueError:
                    self.message = "Amount must be a number"
                    self.account_message()

                if self.amount > 0:
                    pass

                else:
                    self.amount = 0

            account = self.select_account()

            if account:
                self.message = "User already exists, please try again"
                self.account_message()
            else:
                self.create_account()
                self.message = "Your user has been created with acc number: "+ str(self.acc_num)
                self.account_message()


        except Exception as ex:
            errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}\nThere was and issue connecting to your database, please try again later"
            self.message = errormessage.format(type(ex).__name__, ex.args)

    def select_account(self):
        mycursor = mydb.cursor()
        check_user = "SELECT id FROM users WHERE name = '%s'" % (self.acc_holder)
        mycursor.execute(check_user)
        results = mycursor.fetchall()

        if len(results) > 0:
            self.id = results[0]
            return True
        else:
            return False

    def create_account(self):
        mycursor = mydb.cursor()

        command = 'INSERT INTO users(name,password,amount) VALUES("%s","%s","%d")' % (
        self.acc_holder, self.password, self.amount)
        print(command)
        mycursor.execute(command)
        mydb.commit()
        self.id = mycursor.lastrowid

    def auth_user(self,username,password):
        mycursor = mydb.cursor()
        check_user = "SELECT * FROM users WHERE id = '%d'" % (self.id)
        mycursor.execute(check_user)
        result = mycursor.fetchall()

        if len(result) > 0:
            print(result[0])
        else:
            print()

        pass

    def withdraw(self, amount):

        mycursor = mydb.cursor()
        self.amount -= amount

        mycursor.execute("UPDATE amount WHERE id = '%d'") %(self.id)
        return str(amount) + " has been withdrawn from the account. " + str(self.amount) + " is available."


    def deposit(self, amount):
        self.amount += amount

    def account_message(self):
        message = self.message
        return message