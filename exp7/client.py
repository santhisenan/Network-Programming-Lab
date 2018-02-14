# client
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get a local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on port
s.connect((host, port)) 

# recieve no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("Time got from the server is %s" % tm.decode('ascii'))