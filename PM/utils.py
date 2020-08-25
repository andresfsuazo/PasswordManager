import os
import binascii
import sys
from os import system, name

def exit_app():
    sys.exit()

def clear():
    """Clear the terminal screen"""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def new_salt():
    return binascii.hexlify(os.urandom(16))

def decode_salt(salt):
    return salt.decode()

def boxed_text(func):
    def inner(dict):
        print("\n")
        print("*" * 30)
        func(dict)
        print("*" * 30)
        print("\n")
    return inner

def single_dict_key(dict):
    return [a for a, b in dict.items()][0]