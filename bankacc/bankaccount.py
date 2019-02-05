import uuid
#TODO add database of accounts and their values and id's


class BankAcc:
    def __init__(self, name, password, amount,mydb):
        try:
            self.acc_holder = name
            self.acc_num = str(uuid.uuid4())
            #self.acc_type = typeacc

            if amount:
                self.amount = amount
            else:
                self.amount = 0
            mycursor = mydb.cursor()
            check = "SELECT * FROM users WHERE name = '%s'" %(name.get())
            mycursor.execute(check)
            results = mycursor.fetchall()
            if len(results) > 0:
                print("Account already exists")
            else:
                command = "INSERT INTO users(name,password,amount) VALUES('%s','%s','%d')" % (
                name.get(), password.get(), int(amount.get()))
                mycursor.execute(command)
                mydb.commit()
                print("Your account has been created with the id: " + self.acc_num )

        except Exception as ex:
            errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
            message = errormessage.format(type(ex).__name__, ex.args)
            print("There was an issue connecting to your database, please try again later")
            print(message)

    def withdraw(self, amount):
        self.amount -= amount

        return self.amount

    def deposit(self, amount):
        self.amount += amount

    def account_ops():
        print("Account operations:")
        print("1 - Withdraw")
        print("2 - Deposit ")
        print("3 - Back")