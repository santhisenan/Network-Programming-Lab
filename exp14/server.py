import socket
import threading
import os

def recvFile(name, sock):
    filename = sock.recv(1024)
    if(os.path.isfile(filename)):
        sock.send("EXISTS" + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if(userResponse[:2] == "OK"):
            with open(filename, "rb") as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while(bytesToSend != ""):
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR")
    sock.close()

HOST = '127.0.0.1'
PORT = 5000

s = socket.socket()
s.bind((HOST,PORT))

s.listen(10)

print "Server running..."
while True:
    conn, addr = s.accept()
    print "Client "+str(addr)+" connected"
    t = threading.Thread(target=recvFile, args=("retrFile", conn))
    t.start()

s.close()

