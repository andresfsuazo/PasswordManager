from os import path
from PM.PMClient.client import Client
import abc
import json

"""
Interface for both terminal use and Graphical Interface
"""


class UserInterface(metaclass=abc.ABCMeta):

    @classmethod
    def version(cls):
        """User interface version"""
        return "1.0"

    def __init__(self):
        self.mainMenu = ""
        self.client = Client()
        self.settings = {}
        self.set_settings()
        self.username = ""
        self.password = ""

    def set_settings(self):
        """Configure interface using an external, user editable file"""
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))
        else:
            with open("menu_settings.json", "w") as file:
                json.dump(self.settings, file, indent=4)

        self.client.Port = self.settings["Port"]
        self.client.IP_address = self.settings["IP"]
        self.mainMenu = self.settings['main_menu']
        self.client.connect()

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
