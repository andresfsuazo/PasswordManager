import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from utils import *
from cryptography.hazmat.primitives import hashes


class Keys:

    def __init__(self):
        self.key = ""
        self.iterations = 100000

    def create_key(self, salt, pwd):
        pwd = pwd.encode()  # convert to bytes
        salt += pwd
        key_derivation = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                    length=32,
                                    salt=salt,
                                    iterations=self.iterations,
                                    backend=default_backend())
        return b64e(key_derivation.derive(pwd))

    def load_universal_key(self, salt, universal_pwd):
        # Loads the user access key when logging in
        self.key = self.create_key(salt, universal_pwd)

    def encrypt_account(self, salt, universal_pwd, account_pwd):
        # Encrypt password for a specific source
        universal_pwd = universal_pwd.encode() # convert to bytes
        account_pwd = account_pwd.encode()
        salt += universal_pwd
        return b64e(b'%b%b%b' % (salt, self.iterations.to_bytes(4, 'big'), b64d(Fernet(self.key).encrypt(account_pwd))))

    def decrypt_account(self, salt, universal_pwd, account_pwd):
        # Decrypt password for a specific source
        decoded = b64d(account_pwd)
        start_slice = 16 + len(universal_pwd.encode()) + 4
        account_pwd = b64e(decoded[start_slice:])
        return Fernet(self.key).decrypt(account_pwd)

    def get_key(self):
        return self.key

