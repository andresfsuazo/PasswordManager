# Python program to implement client side of chat room.
import socket

'''
Sends requests to server
'''


class Client:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(3.0)  # 3 second timeout for each socket operation
        # self.IP_address = "3.129.136.42"
        self.IP_address = "0.0.0.0"  # Server IP
        self.Port = 7788  # Server Port

    def connect(self):
        try:
            self.server.connect((self.IP_address, self.Port))
        except socket.error:
            print("Can't connect to server")

    def close(self):
        self.server.close()

    def send_command(self, cmd, **kwargs):
        one = cmd
        # Send arguments
        for i in kwargs:
            one += "|^|" + i
            one += "|^|" + kwargs[i]
        self.server.sendall(one.encode())

        response = self.receive_response()
        if response not in ("0", "1"):
            return response
        else:
            return True if response == "1" else False

    def receive_response(self):
        message = self.server.recv(2048)
        return message.decode()
