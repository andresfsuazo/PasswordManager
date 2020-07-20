# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
import json
from os import path
from utils import *
from serversim import Keys

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
        message = "Connected to password manager"
        conn.sendall(message.encode())

        while True:
            try:
                command = conn.recv(2048)
                print("command = " + command)
                if command:

                    """prints the message and address of the 
                    user who just sent the message on the server 
                    terminal"""
                    print
                    "<" + addr[0] + "> " + command

                    # Calls broadcast function to send message to all
                    message_to_send = "<" + addr[0] + "> " + command
                    self.broadcast(message_to_send, conn)

                else:
                    """message may have no content if the connection 
                    is broken, in this case we remove the connection"""
                    self.remove(conn, addr[0])

            except:
                continue

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
        if cmd == "login":
            print("Log In Attempt")
            self.log_in(kwargs["user"], kwargs["pwd"])
        elif cmd == "new":
            print("New Account Attempt")
            self.log_in(kwargs["user"], kwargs["pwd"])

    def log_in(self, user, pwd):
        '''
        Login to an existing account
        '''
        if user not in self.accounts:
            return False
        salt = self.accounts[user]["salt"]
        self.keys.load_universal_key(salt, pwd)
        if self.accounts[user]["password"] == self.keys.get_key():
            #self.user = user
            #self.password = pwd
            return True
        return False

    def create_main(self, user, pwd):
        '''
        Create an account for using the password manager
        '''
        #Create username
        if user in self.usernames:
            return False
        #Creat salt
        salt = new_salt()

        #Get key for password
        self.keys.load_universal_key(salt, pwd)
        self.accounts[user] = {"password": self.keys.get_key(), "salt": salt, "accounts": {}}
        self.SaveUsers()
        return True

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
