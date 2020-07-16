import time
import curses
import json
from os import path

class Menu:
    def __init__(self):
        self.menu = ['Login', 'Create Account', "Exit"]
        self.login = ['Get Credentials','Add Credentials', 'Back', 'Exit']
        self.settings = {'cursor blink': 0, 'exit time': 5}

    def set_settings(self):
        if path.exists('/settings.json'):
            self.settings = json.load(open('/settings.json'))
        else:
            json.dump(self.settings, open('/settings.json', 'w'))

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
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(text) // 2
        y = h // 2
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def build_menu(self, stdscr):
        k = 0
        curses.curs_set(self.settings["cursor blink"])

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(stdscr, current_row, self.menu)
        current_menu = self.menu

        # Loop where k is the last character pressed
        while (k != ord('q')):

            k = stdscr.getch()
            if k == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif k == curses.KEY_DOWN and current_row < len(current_menu)-1:
                current_row += 1
            elif k == curses.KEY_ENTER or k in [10, 13]:
                if current_row == 0:
                    current_menu = self.login

            self.print_menu(stdscr, current_row, current_menu)


    def start_display(self):
        curses.wrapper(self.build_menu)