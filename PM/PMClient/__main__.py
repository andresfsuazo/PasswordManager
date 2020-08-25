import json
from os import path
from PM.PMClient import *


def TerminalMain():
    menu = terminal_interface.TerminalMenu()
    menu.display_menu()


def GUIMain():
    menu = graphical_interface.GUI()
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
