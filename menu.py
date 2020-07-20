import time
import curses
import json
from os import path
from accounts import Accounts
from client import Client

class Menu:

    def __init__(self):
        self.client = Client()
        self.menu_items = {}
        self.current_menu = {}
        self.username = ""
        self.password = ""
        self.settings = {'cursor blink': 0, 'exit time': 5, 'menu items': {
                                                                'Login':{
                                                                    "Get Credentials": "",
                                                                    "Add Credentials": "",
                                                                    "Back": "",
                                                                    "Exit" : ""
                                                                },
                                                                'Create Account':"",
                                                                "Exit":""
                                                                }}

    def set_settings(self):
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))
        else:
            with open("menu_settings.json", "w") as file:
                json.dump(self.settings, file, indent=4)

        self.menu_items = self.settings["menu items"]

    def print_menu(self, stdscr, selected_row_idx, current):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(current):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(current) // 2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    def print_center(self, stdscr, text):
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(text) // 2
        y = h // 2
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def get_input(self, stdscr, hidden=False):
        input = []
        done = False
        while not done:
            key = stdscr.getch()
            if key != 10 and key != curses.KEY_UP and key != curses.KEY_DOWN: #while user does not press enter
                key = chr(key)
                input.append(key)
                if not hidden : stdscr.addstr(str(key))
            else:
                done = True
        return "".join(input)

    def build_menu(self, stdscr):
        k = 0
        curses.curs_set(self.settings["cursor blink"])
        curses.noecho()

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(stdscr, current_row, self.menu_items)
        self.current_menu = self.menu_items

        # Loop where k is the last character pressed
        while k != ord('q'):

            k = stdscr.getch()
            selected_key = list(self.current_menu.keys())[current_row]

            if k == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif k == curses.KEY_DOWN and current_row < len(self.current_menu)-1:
                current_row += 1
            elif k == 10:
                if current_row == len(self.current_menu)-1 and self.current_menu[selected_key] == "":
                    k = ord('q')
                elif selected_key.lower() == "back":
                    self.current_menu = self.menu_items
                else:
                    if type(self.current_menu[selected_key]) is dict:
                        self.current_menu = self.current_menu[selected_key]
                    else:
                        self.function_caller(stdscr, self.current_menu[selected_key])
                    current_row = 0;


            self.print_menu(stdscr, current_row, self.current_menu)

    def submit_credentials(self, new = False):
        args = {"user" : self.username, "pwd" : self.password}
        if new:
            logged_in = self.client.send_command("new", **args)
        else:
            logged_in = self.client.send_command("login", **args)

        new_display = {
            "Get Credentials": "",
            "Add Credentials": "",
            "Back": "",
            "Exit": ""
        }

        if logged_in:
            self.current_menu = new_display
        else:
            self.current_menu = self.menu_items

    def function_caller(self, stdscr, id):
        if id == 0:
            self.username = self.get_input(stdscr)
            self.current_menu = self.menu_items["Login"]
        elif id == 1:
            self.password= self.get_input(stdscr, True)
            self.current_menu = self.menu_items["Login"]
        elif id == 2:
            self.submit_credentials()
        elif id == 3:
            self.username = self.get_input(stdscr)
            self.current_menu = self.menu_items["Create Account"]
        elif id == 4:
            self.password = self.get_input(stdscr, True)
            self.current_menu = self.menu_items["Create Account"]
        elif id == 5:
            self.submit_credentials(True)
        else:
            pass

    def start_display(self):
        curses.wrapper(self.build_menu)