# Python program to implement server side of chat room.
import socket
import pickle
import json
from os import path
from .keys import Keys
from PM.utils import *


class Server:

    def __init__(self):
        self.keys = Keys()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        IP_address = "localhost"
        Port = 8000
        # Port = 7788
        # Binds the server to IP and Port
        self.server.bind((IP_address, Port))
        # Set a max of 10 connections
        self.server.listen(10)
        self.clientList = []
        self.accounts = {}
        self.load_users()

    def load_users(self):
        if path.exists('PM/PMServer/accounts.json'):
            self.accounts = json.load(open('PM/PMServer/accounts.json'))
        else:
            with open("PM/PMServer/accounts.json", "w") as file:
                json.dump(self.accounts, file, indent=4)

    def save_users(self):
        with open("PM/PMServer/accounts.json", "w") as file:
            json.dump(self.accounts, file, indent=4)

    def client_thread(self, conn, addr):
        # sends a message to the client whose user object is conn
        # message = "Connected to password manager"
        # conn.sendall(message.encode())
        while True:
            try:
                # Receive pickled data from client
                data = conn.recv(4096)
                data = pickle.loads(data)
                if data:
                    command = data.pop("command")
                    message = self.commands(command, **data)  # Execute a specific function
                    print("To return: ", message)
                    message = pickle.dumps(message)  # Pickle and send message to client
                    conn.sendall(message)
                else:
                    print("Empty message sent to server")
                    self.remove(conn, addr[0])
                    break

            # except ConnectionError
            except:
                print("Connection Error")
                self.remove(conn, addr[0])
                break

    def broadcast(self, message, connection):
        """Send a message to all connected clients"""
        for clients in self.clientList:
            if clients != connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    self.remove(clients)

    def remove(self, connection, addr):
        """Remove connected client from server"""
        if connection in self.clientList:
            self.clientList.remove(connection)
            print((addr + " disconnected"))

    def commands(self, cmd, **kwargs):
        validated = False

        if cmd == "login":
            validated = self.log_in(kwargs["user"], kwargs["pwd"])
            print("Log In Attempt: " + kwargs["user"] + " - " + str(validated))
        elif cmd == "new":
            validated = self.create_main(kwargs["user"], kwargs["pwd"])
            print("New Account: " + kwargs["user"] + " - " + str(validated))
        elif cmd == "newsub":
            validated = self.create_sub(kwargs["user"], kwargs["pwd"], kwargs["account"], kwargs["usersub"],
                                        kwargs["pwdsub"])
            print("New Sub Attempt: " + kwargs["user"] + " - " + kwargs["account"])
        elif cmd == "getsub":
            validated = self.get_sub(kwargs["user"], kwargs["account"], kwargs["pwd"])
            print("Account Sent: " + kwargs["user"] + " -> " + str(validated))
        elif cmd == "getall":
            validated = self.get_all(kwargs["user"])
            print("Accounts Loaded: " + kwargs["user"])

        return validated

    def log_in(self, user, pwd):
        """Login to an existing account"""
        if user not in self.accounts:
            return False
        salt = self.accounts[user]["salt"]
        salt = salt.encode()
        password = self.accounts[user]["password"]
        password = password.encode()
        key = self.keys.create_key(salt, pwd)

        if password == key:
            return True
        return False

    def create_main(self, user, pwd):
        """Create an account for using the password manager"""
        if user in self.accounts: return False  # Check if username available
        salt = new_salt()  # Create salt
        key = self.keys.create_key(salt, pwd)  # Get key for password
        password = key
        password = password.decode()
        self.accounts[user] = {"password": password, "salt": salt.decode(), "accounts": {}}
        self.save_users()
        return True

    def create_sub(self, user, pwd, account, usersub, pwdsub):
        """Create an account for using the password manager """
        account = str(account).lower()
        if account in self.accounts[user]["accounts"]: return False  # Check if name available
        salt = new_salt()  # Create salt
        pwdsub = self.keys.encrypt_account(salt, pwd, pwdsub)
        self.accounts[user]["accounts"][account] = {"username": usersub, "password": pwdsub.decode()}
        self.save_users()
        return True

    def get_sub(self, user, account, pwd):
        """Retrieve a username and password for a specific site"""
        if account in self.accounts[user]["accounts"]:
            username = self.accounts[user]["accounts"][account]["username"]
            password = self.accounts[user]["accounts"][account]["password"]

            # decrypt password
            password = self.keys.decrypt_account(pwd, password)
            return [username, password.decode()]
        else:
            return False

    def get_all(self, user):
        """Retrieves a list of all users accounts"""
        return [account for account in self.accounts[user]["accounts"]]
