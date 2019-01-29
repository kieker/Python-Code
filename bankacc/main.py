from bankaccount import BankAcc
import mysql.connector

def dbfunc():
    mydb = mysql.connector.connect(
        host="sql1.jnb3.host-h.net",
        user="kieketehht_4",
        passwd="uVv4MZ4rER6NEfAaKtb8",
        database="kieketehht_pyt"
    )
    try:
        mycursor = mydb.cursor()
        mycursor.execute("USE kieketehht_pyt")
        mycursor.execute("SHOW TABLES")
        results  = mycursor.fetchall()
        print("All Tables currently in Database: ",results)
        results_list = [item[0] for item in results]

        if "users" not in results_list:
            mycursor.execute("CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),password VARCHAR(255))")
            print("Users table created")
        else:
            print("Users table already exist")

    except Exception as ex:
        errormessage = "An exception of type {0} occurred. Arguments: \n{1!r}"
        message = errormessage.format(type(ex).__name__,ex.args)
        print("There was an issue connecting to your database, please try again later")
        print(message)






def choice_validate(value: str):
    while value.upper() not in choices:
        value = input("Invalid choice. Please try again. Y/N: ")
    return value


choices = ("Y", "N")
dbfunc()
while True:

    user_option = input("Hi, would you like to create an account? Y/N: ")

    user_option = choice_validate(user_option)

    if user_option.upper() == "Y":
        name = input("What is the account holder's name: ")
        acc_type = input("What is preferred account type: ")
        amount_flag = input('Do you want to deposit some money into this account now? Y/N: ')

        amount_flag = choice_validate(amount_flag)

        if amount_flag.upper() == "Y":
            amount = int(input("What is the amount that you want to deposit: "))
            while amount < 0:
                amount = input("Money deposited cannot be negative. Please try again: ")
            acc1 = BankAcc(name, acc_type, amount)

        else:
            acc1 = BankAcc(name, acc_type, 0)

        BankAcc.account_ops()

        choice = input("Please make a choice of operations: ")
        if choice.upper() == "E":
            continue
        else:
            choice = int(choice)
        while 1 > choice < 3:
            BankAcc.account_ops()

            choice = int(input("Wrong choice made. Please try again : "))

    if user_option.upper() == "N":
        use_acc = input("Access a previous account? Y/N: ")
        use_acc = choice_validate(use_acc)
        if use_acc.upper() == "Y":
            which_account = input("Which Account would you like to access?")

        # TODO ask user for name and access that account

        if use_acc.upper() == 'N':
            print("Thank you, banking will now close")
            exit(1)
        elif use_acc.upper() == 'Y':
            # TODO implement reading data from database and accessing object methods
            print("using account")
