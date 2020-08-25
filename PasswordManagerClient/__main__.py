import json
from os import path
from PasswordManagerClient.terminal import TerminalMenu
from PasswordManagerClient.GUI import GUI


def TerminalMain():
    menu = TerminalMenu()
    menu.display_menu()


def GUIMain():
    menu = GUI()
    menu.display_menu()


mode = 0
try:
    if path.exists('menu_settings.json'):
        settings = json.load(open('menu_settings.json'))
        mode = settings["interaction mode"]
except KeyError:
    print("Key Error")
except Exception as e:
    print("Unhandled exception: ", e)

GUIMain() if mode == 0 else TerminalMain()
