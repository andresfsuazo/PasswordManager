"""
    Andres Suazo
    Handles interaction between user and program
"""
from cryptography.fernet import Fernet
from hashlib import sha256
from serversim import Keys
from accounts import Accounts


class Menu:

    def __init__(self):
        self.accounts = Accounts()
        self.running = True
        self.menu_options = {
            0: "Exit",
            1: "Log In",
            2: "New Account",
            3: "New Sub",
            4: "Get Account",
            9: "Print accounts"
        }  # used to add new features to program

    def menu_call(self, c):
        if c == 0:
            self.running = False
        elif c == 1:
            self.log_in()
        elif c == 2:
            self.new_user()
        elif c == 3:
            # new sub
            self.new_sub()
        elif c == 4:
            # get sub
            self.get_sub()
        elif c == 5:
            self.new_user()
        elif c == 6:
            self.new_user()
        elif c == 7:
            self.new_user()
        elif c == 8:
            self.new_user()
        elif c == 9:
            self.print_accounts()
        else:
            pass

    def main_loop(self):
        while self.running:
            for i in self.menu_options:
                print("{}:{}".format(i, self.menu_options[i]))
            c = input("Enter option: ")
            c = int(c)
            self.menu_call(c)

    def new_user(self):
        self.accounts.create_main()

    def log_in(self):
        self.accounts.log_in()

    def print_accounts(self):
        self.accounts.print_accounts()

    def new_sub(self):
        name = input("Account name: ")
        username = input("username: ")
        password = input("password: ")
        self.accounts.create_sub(name, username, password)

    def get_sub(self):
        account = input("Account name: ")
        response = self.accounts.get_sub(account)
        print("username: {}, password: {}".format(response[0], response[1])) if response != 0 else print("Not found!")


def main():
    # Start application
    menu = Menu()
    menu.main_loop()

