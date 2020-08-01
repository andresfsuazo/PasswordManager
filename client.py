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
        one = cmd
        #Send arguments
        for i in kwargs:
            one+="|^|"+i
            one+="|^|"+kwargs[i]
        self.server.sendall(one.encode())

        response = self.receive_response()
        if response != "0" and response != "1":
            return response
        else:
            return True if response == "1" else False

    def receive_response(self):
        message = self.server.recv(2048)
        return message.decode()