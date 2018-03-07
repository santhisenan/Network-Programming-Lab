import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    # ClientSocket, addr = sock.accept()
    message, ClientSocket = sock.recvfrom(1024) # buffer size is 1024 bytes
    CurrentTime = time.ctime(time.time()) + "\r\n"
    sock.sendto(CurrentTime.encode('ascii'),ClientSocket)
    # sock.close()