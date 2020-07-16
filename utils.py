import os
import base64
import re

def new_salt():
    return os.urandom(16)

def boxed_text(func):
    def inner(dict):
        print("\n")
        print("*" * 30)
        func(dict)
        print("*" * 30)
        print("\n")
    return inner
