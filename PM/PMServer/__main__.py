from PM.PMServer import *

try:
    import thread
except ImportError:
    import _thread as thread

server = server.Server()
print("Server Started")

while True:
    conn, addr = server.server.accept()
    server.clientList.append(conn)
    print(addr[0] + " connected")
    thread.start_new_thread(server.client_thread, (conn, addr))  # Each connected user represents a thread
