import sys
from os import system, name, path
import json
from utils import *
from client import Client


def exit_app():
    sys.exit()


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def build_menu(current_menu):
    for key in current_menu:
        print("{}. {}".format(key, single_dict_key(current_menu[key])))
    print("\n0. Quit")


class TerminalMenu:
    def __init__(self):
        self.client = Client()
        self.mainMenu = {}
        self.current_menu = {}
        self.inputs = []
        self.username = ""
        self.password = ""
        self.settings = {
            "terminal mode": 1,
            'main_menu': {
                "1": {'Login': 'login'},
                "2": {'Create Account': 'createAccount'}
            },
            'sub_menu': {
                "home": {
                    "1": {"Get Credentials": 'getAccount'},
                    "2": {"Add Credentials": 'addAccount'}
                },
            }
        }

    def begin_display(self):
        self.set_settings()
        self.main_menu()

    def set_settings(self):
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))
        else:
            with open("menu_settings.json", "w") as file:
                json.dump(self.settings, file, indent=4)

        self.mainMenu = self.settings['main_menu']

    def call_me(self, arg):
        return getattr(self, arg)()

    # Main menu
    def main_menu(self):
        clear()  # Clear terminal window
        print("Password Manager\n")  # Title

        # Set current menu to return to if any input problems
        self.current_menu = "main_menu"

        # Menu Options
        build_menu(self.mainMenu)

        choice = input(" >>  ")
        self.function_call(choice)

        return

    # Sub Menu
    def sub_menu(self, name):
        '''
        Build a sub-menu from json file
        '''
        clear()  # Clear terminal window
        print(name.capitalize())  # Title

        # Set current menu to return to if any input problems
        self.current_menu = name

        # Menu Options
        build_menu(self.settings["sub_menu"][name])

        choice = input(" >>  ")
        self.function_call(choice)

        return

    def results_page(self, results):
        clear()

        #Print Resutls line by line
        for i in results: print(i)

        #Build an empty menu with only exit and back options
        build_menu({"1": {"Back": "back"}})

        while True:
            choice = input(" >>  ")
            ch = choice.lower()

            if ch == "0":
                exit_app()
                return
            elif ch == "1":
                self.back()
                return
            else:
                print("Invalid selection, please try again.\n")

    # Processing of user input
    def function_call(self, entered):
        clear()
        ch = entered.lower()
        if ch == "0":
            exit_app()
        else:
            try:
                if self.current_menu != "main_menu":
                    to_call = single_dict_key(self.settings["sub_menu"][self.current_menu][ch])
                    to_call = self.settings["sub_menu"][self.current_menu][ch][to_call]
                    self.call_me(to_call)
                else:
                    to_call = single_dict_key(self.settings["main_menu"][ch])
                    to_call = self.settings["main_menu"][ch][to_call]
                    self.call_me(to_call)
            except KeyError:
                print("Invalid selection, please try again.\n")
                self.sub_menu("home") if self.current_menu != "main_menu" else self.main_menu()
        return

    def login(self):
        self.username = input("Username: ")
        self.password = input("Password: ")
        args = {"user": self.username, "pwd": self.password}
        logged_in = self.client.send_command("login", **args)

        # If login credential accepted go to home menu
        if logged_in:
            self.sub_menu("home")
        else:
            self.login();

    def createAccount(self):
        self.username = input("Set Username: ")
        self.password = input("Set Password: ")
        args = {"user": self.username, "pwd": self.password}
        logged_in = self.client.send_command("new", **args)

        # If login credential accepted go to home menu
        if logged_in != "0":
            self.sub_menu("home")
        else:
            self.createAccount();

    def getAccount(self):
        account = input("Account Name: ")
        args = {"user": self.username, "pwd": self.password, "account": account}
        response = self.client.send_command("getsub", **args)
        print(response)
        response = response.split("|^|")

        if response:
            results = [
                "Account Name: " + account,
                "Username: " + response[0],
                "Password: " + response[1]
            ]

        else:
            results = [
                "No account named: " + account
            ]

        self.results_page(results)

    def addAccount(self):
        account = input("Account Name: ")
        username = input("Account Username: ")
        pwd = input("Account Password: ")
        args = {"user": self.username, "pwd": self.password, "account": account, "usersub": username, "pwdsub": pwd}
        response = self.client.send_command("newsub", **args)

        if response:
            results = [
                "Account Credentials Saved!"
            ]

        else:
            results = [
                "Account name in use"
            ]

        self.results_page(results)

    def back(self):
        self.sub_menu("home")