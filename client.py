# Python program to implement client side of chat room.
import socket
import select
import sys

'''
Sends requests to server
'''
class Client():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # takes the first argument from command prompt as IP address
        self.IP_address = "127.0.0.1"
        # takes second argument from command prompt as port number
        self.Port = 65432
        self.server.connect((self.IP_address, self.Port))

    def close(self):
        self.server.close()

    def send_command(self, cmd, **kwargs):
        self.server.send(cmd.encode())

    def recieve_response(self):
        message = self.server.recv(2048)
        print(message)