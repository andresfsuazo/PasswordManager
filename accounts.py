import os
from utils import *
from serversim import Keys

class Accounts:
    def __init__(self):
        self.keys = Keys()
        self.usernames = {"andres": {'password': b'zNHyl6kYhlAiTxZe4xMiUETdqhTjYqW69Tx_aW75rmw=', 'salt': b'\xfcjp{\x9d\xfeK2\x18\x94\x86DK\x0f|\xc5', 'accounts': {}}}
        self.user = ""
        self.password = ""

    @boxed_text
    def print_accounts(self):
        for i in self.usernames:
            print("username: {} | password: {}".format(i, self.usernames[i]))

    def log_in(self, user, pwd):
        '''
        Login to an existing account
        '''
        # Ask user for name and password
        # Generate key to be used in the program

        # user = input("Enter username: ")
        # while user not in self.usernames:
        #     print("User not found!")
        #     user = input("Enter username: ")

        if user not in self.usernames:
            return False

        # pwd = input("Enter password: ")
        # correct = False
        salt = self.usernames[user]["salt"]
        self.keys.load_universal_key(salt, pwd)
        if self.usernames[user]["password"] == self.keys.get_key():
            self.user = user
            self.password = pwd
            return True

        # while not correct:
        #     self.keys.load_universal_key(salt, pwd)
        #     if self.usernames[user]["password"] == self.keys.get_key():
        #         print("Logged in!")
        #         self.user = user
        #         self.password = pwd
        #         correct = True
        #     else:
        #         print("Incorrect Password!")
        #         pwd = input("Enter password: ")

        return False

    def create_main(self):
        '''
        Create an account for using the password manager
        '''
        user = input("Enter username: ")

        #Create username
        while user in self.usernames:
            print("Not available, enter new username!")
            user = input("username: ")
        #Create password
        pwd = input("Enter password: ")
        #Creat salt
        salt = new_salt()

        #Get key for password
        self.keys.load_universal_key(salt, pwd)
        self.usernames[user] = {"password": self.keys.get_key(), "salt": salt, "accounts": {}}
        print("User created: " + user)

    def create_sub(self, name, user, password):
        '''
        Create a username password entry for a specific site
        '''
        # get salt
        salt = self.usernames[self.user]["salt"]
        # add account
        name = str(name).lower()
        # encrypt password
        password = self.keys.encrypt_account(salt, self.password, password)
        self.usernames[self.user]["accounts"][name] = {"username": user, "password": password}

    def get_sub(self, name):
        """
        Retrieve a username and password for a specific site
        """
        if name in self.usernames[self.user]["accounts"]:
            username = self.usernames[self.user]["accounts"][name]["username"]
            password = self.usernames[self.user]["accounts"][name]["password"]
            salt = self.usernames[self.user]["salt"]

            # decrypt password
            password = self.keys.decrypt_account(salt, self.password, password)

            return [username, password.decode()]
        else:
            return 0


