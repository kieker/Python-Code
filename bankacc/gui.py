import tkinter as tk
from bankaccount import BankAcc

class Gui:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Banking system")
        self.win.geometry("500x300")

    def main_gui(self):
        self.reset_window()
        tk.Label(self.win, text="Welcome to the Banking system").pack()
        tk.Button(self.win, text="Login using existing account", width=50).pack()
        tk.Button(self.win, text="Create a new account", width=50, command=lambda: self.account_create()).pack()
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

    def account_create(self):

        self.reset_window()
        tk.Label(self.win, text="Please enter the account holder name").pack()
        username = tk.Entry(self.win)
        username.pack()

        tk.Label(self.win, text="Please enter your password").pack()
        password = tk.Entry(self.win, show="*")
        password.pack()

        tk.Label(self.win, text="Please enter the amount that you want to deposit")
        amount = tk.Entry(self.win)
        amount.pack()

        account = tk.Button(self.win, text="Create Account", command=lambda: self.create_user(username, password, amount)).pack()
        self.back_to_main_button()

    def back_to_main_button(self):
        back_button = tk.Button(text="Back to main menu", command=self.main_gui)
        back_button.pack()

    def create_user(self, username, password, amount):
        account = BankAcc(username, password, amount)
        return account