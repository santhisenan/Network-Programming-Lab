import socket
import time

# create a socket object
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
ServerSocket.bind((host, port))

ServerSocket.listen(5)

while True:
    # establish a connection
    ClientSocket, addr = ServerSocket.accept()

    print("Got a connection from %s" % str(addr))
    CurrentTime = time.ctime(time.time()) + "\r\n"
    ClientSocket.send(CurrentTime.encode('ascii'))
    ClientSocket.close()

