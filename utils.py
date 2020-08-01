import os
import binascii

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