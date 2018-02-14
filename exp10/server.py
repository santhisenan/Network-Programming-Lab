import socket
import time

# create a server object
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#get local machine name
host = socket.gethostname()

port = 5005

#bind to port
ServerSocket.bind((host, port))

while True:
    data, addr = ServerSocket.recvfrom(1024)
    print(data)
    print addr


