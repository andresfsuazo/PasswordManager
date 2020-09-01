# Python program to implement client side of chat room.
import socket
import pickle

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
        # Send command and arguments as dictionary
        message = {"command": cmd}
        for key in kwargs:
            message[key] = kwargs[key]

        # Send pickled data to server
        message = pickle.dumps(message)
        self.server.sendall(message)

        # Get response from server
        response = self.receive_response()
        return response

    def receive_response(self):
        message = self.server.recv(4096)
        return pickle.loads(message)
