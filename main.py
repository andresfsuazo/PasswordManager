import menu
from terminal import TerminalMenu
import client

def menumain():
    console_menu = menu.Menu()
    console_menu.set_settings()
    console_menu.start_display()

def main():
    menu = TerminalMenu()
    menu.begin_display()

if __name__ == "__main__":
    main()