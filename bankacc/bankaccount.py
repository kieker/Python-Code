import uuid
#TODO add database of accounts and their values and id's


class BankAcc:
    def __init__(self, name, typeacc, amount):
        try:
            self.acc_holder = name
            self.acc_num = str(uuid.uuid4())
            self.acc_type = typeacc

            if amount:
                self.amount = amount
            else:
                self.amount = 0

            print("Your account has been created with the id: " + self.acc_num )

        except:
            print('There was a problem creating your account')

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