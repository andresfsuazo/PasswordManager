from os import path
from client import Client
import abc
import json

"""
Interface for both terminal use and Graphical Interface
"""


class UserInterface(metaclass=abc.ABCMeta):

    @classmethod
    def version(self):
        """User interface version"""
        return "1.0"

    def __init__(self):
        self.client = Client()
        self.username = ""
        self.password = ""

    def set_settings(self):
        """Configure interface using an external, user editable file"""
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))
        else:
            with open("menu_settings.json", "w") as file:
                json.dump(self.settings, file, indent=4)

        self.mainMenu = self.settings['main_menu']

    @abc.abstractmethod
    def display_menu(self):
        """Start the display that the user will interact with"""
        pass

    @abc.abstractmethod
    def login(self):
        """Send Login information to server and wait for confirmation"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_account(self):
        """Send account information for a new account to server and wait for confirmation"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_account(self):
        """Gets account information from server"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_account(self):
        """Add account information in server"""
        raise NotImplementedError
