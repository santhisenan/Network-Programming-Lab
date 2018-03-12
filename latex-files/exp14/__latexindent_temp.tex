import socket

HOST = "127.0.0.1"
PORT = 5000

s = socket.socket()
s.connect((HOST, PORT))

filename = raw_input("Enter the filename: ")
if(filename != 'q'):
    s.send(filename)
    data = s.recv(1024)
    if(data[:6] == "EXISTS"):
        filesize = long(data[6:])
        message = raw_input("File is present in the server. Do you want to download? (y/n) :")  
        if(message == 'y'):
            s.send("OK")
            f = open("recv_" + filename, "wb")
            data = s.recv(1024)
            totalReceived = len(data)
            f.write(data)
            while totalReceived < filesize:
                data = s.recv(1024)
                totalReceived += len(data)
                f.write(data)
            print "Download complete"
    else:
        print "File is not present in the server"
s.close()
