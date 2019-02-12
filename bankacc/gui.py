import tkinter as tk
from bankaccount import BankAcc

class Gui:

    def __init__(self):

        self.win = tk.Tk()
        self.win.title("Banking system")
        self.win.geometry("500x300")
        self.account = False

    def main_gui(self):

        self.reset_window()
        #img = ImageTK.photoImage
        tk.Label(self.win, text="Welcome to the Banking system", font=("Open Sans",21)).pack()
        login = tk.Button(self.win, text="Login using existing account", width=50, command=self.login_account, relief="groove")
        login.place(relx=0.5, rely=0.4, anchor="center")
        create = tk.Button(self.win, text="Create a new account", width=50, command=lambda: self.account_create(), relief="groove")
        create.place(relx=0.5, rely=0.6, anchor="center")
        self.win.mainloop()

    def all_children(self):

        _list = self.win.winfo_children()
        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())
        return _list

    def reset_window(self):

        widget_list = self.all_children()
        for item in widget_list:
            item.pack_forget()
            item.place_forget()

    def back_to_main_button(self):

        back_button = tk.Button(text="Back to main menu", command=self.main_gui, relief="groove" )
        back_button.pack(side=tk.BOTTOM)


    def account_create(self):

        self.reset_window()
        tk.Label(self.win, text="Create your account",font=("Open Sans", 21)).pack()
        tk.Label(self.win, text="Please enter the account holder name").pack()
        username = tk.Entry(self.win)
        username.pack()

        tk.Label(self.win, text="Please enter your password").pack()
        password = tk.Entry(self.win, show="*")
        password.pack()

        tk.Label(self.win, text="Please enter the amount that you want to deposit").pack()
        amount = tk.Entry(self.win)
        amount.pack()

        tk.Button(self.win, text="Create Account", command=lambda: self.create_user(username, password, amount), relief="groove").pack()
        self.back_to_main_button()
        # account = self.login_user(username,password)
        if self.account:
            tk.Button(self.win, text="Login to your Account", command=lambda: self.create_user(username, password, amount),
                      relief="groove").pack()
        return username.get(),password.get(),amount.get()


    def create_user(self, username, password, amount):
        account = BankAcc(username, password, amount)
        account_create = tk.Label(self.win, text=account.account_message()).pack()
        string_contain = "exception"
        if string_contain not in account.account_message():
            self.account = True
        return account

    def login_account(self):
        self.reset_window()
        tk.Label(self.win, text="Login to account",font=("Open Sans", 21)).pack()

        tk.Label(self.win, text="Username").pack()
        u_name = tk.Entry(self.win)
        u_name.pack()

        tk.Label(self.win, text="Password").pack()
        p_word = tk.Entry(self.win,show="*")
        p_word.pack()

        tk.Button(self.win, text="Login", command=lambda: self.login_user(u_name,p_word),relief="groove").pack()

        self.back_to_main_button()

    def login_user(self, username, password):

        account = BankAcc(username, password)
        account_login = tk.Label(self.win, text=account.account_message()).pack()
        return account

    def account_ops(self):

        self.reset_window()

        heading = tk.Label(text="Account Operations")
        heading.pack()

        withdraw = tk.Button(text="Withdraw", command="withdraw_render", relief="groove")
        withdraw.pack()

        deposit = tk.Button(text="Deposit", command="deposit_render", relief="groove")
        deposit.pack()

        self.back_to_main_button()


