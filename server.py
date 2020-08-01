# Python program to implement server side of chat room.
import socket
from _thread import *
import json
from os import path
from utils import *
from Keys import Keys


class Server:

    def __init__(self):
        self.keys = Keys()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # takes the first argument from command prompt as IP address
        IP_address = "127.0.0.1"
        # takes second argument from command prompt as port number
        Port = 65432
        # Binds the server to IP and Port
        self.server.bind((IP_address, Port))
        # Set a max of 10 connections
        self.server.listen(10)
        self.clientList = []
        self.accounts = {}

        if path.exists('accounts.json'):
            self.accounts = json.load(open('accounts.json'))
        else:
            with open("accounts.json", "w") as file:
                json.dump(self.accounts, file, indent=4)

    def SaveUsers(self):
        with open("accounts.json", "w") as file:
            json.dump(self.accounts, file, indent=4)

    def clientthread(self, conn, addr):
        # sends a message to the client whose user object is conn
        # message = "Connected to password manager"
        # conn.sendall(message.encode())
        while True:
            try:
                command = conn.recv(2048)
                command = command.decode()
                if command:
                    execute = command.split("|^|")
                    args = {execute[i]: execute[i + 1] for i in range(1, len(execute), 2)}
                    message = self.commands(execute[0], **args)
                    print("to return = ", message)
                    conn.sendall(message.encode())
                else:
                    print("Empty message sent to server")
                    self.remove(conn, addr[0])
                    break

            except ConnectionError:
                print("Connection Error")
                self.remove(conn, addr[0])
                break

    def broadcast(self, message, connection):
        for clients in self.clientList:
            if clients != connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    # if the link is broken, we remove the client
                    self.remove(clients)

    def remove(self, connection, addr):
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
            if validated != False: return validated

        print(validated)
        if validated:
            return "1"
        else:
            return "0"

    def log_in(self, user, pwd):
        '''
        Login to an existing account
        '''
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
        '''
        Create an account for using the password manager
        '''
        if user in self.accounts: return False  # Check if username available
        salt = new_salt()  # Create salt
        key = self.keys.create_key(salt, pwd)  # Get key for password
        password = key
        password = password.decode()
        self.accounts[user] = {"password": password, "salt": salt.decode(), "accounts": {}}
        self.SaveUsers()
        return True

    def create_sub(self, user, pwd, account, usersub, pwdsub):
        '''
        Create an account for using the password manager
        '''
        account = str(account).lower()
        if account in self.accounts[user]["accounts"]: return False  # Check if name available
        salt = new_salt()  # Create salt
        pwdsub = self.keys.encrypt_account(salt, pwd, pwdsub)
        self.accounts[user]["accounts"][account] = {"username": usersub, "password": pwdsub.decode()}
        self.SaveUsers()
        return True

    def get_sub(self, user, account, pwd):
        """
        Retrieve a username and password for a specific site
        """
        if account in self.accounts[user]["accounts"]:
            username = self.accounts[user]["accounts"][account]["username"]
            password = self.accounts[user]["accounts"][account]["password"]

            # decrypt password
            password = self.keys.decrypt_account(pwd, password)
            return username+"|^|"+password.decode()
        else:
            return False


def main():
    server = Server()
    while True:
        conn, addr = server.server.accept()
        server.clientList.append(conn)

        # prints the address of the user that just connected
        print(addr[0] + " connected")

        # creates and individual thread for every user
        # that connects
        start_new_thread(server.clientthread, (conn, addr))

    conn.close()
    server.close()


if __name__ == '__main__':
    main()
