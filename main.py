import json
from os import path
from terminal import TerminalMenu
from GUI import GUI

def TerminalMain():
    menu = TerminalMenu()
    menu.display_menu()

def GUIMain():
    menu = GUI()
    menu.display_menu()

def main():
    mode = 0
    if path.exists('menu_settings.json'):
        settings = json.load(open('menu_settings.json'))
        mode = settings["interaction mode"]
    GUIMain() if mode == 0 else TerminalMain()


if __name__ == "__main__":
    main()