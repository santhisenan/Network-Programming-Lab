import socket
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3000

clientSocket = socket.socket()
clientSocket.connect((SERVER_HOST, SERVER_PORT))

def printMessageFromServer():        
    message = clientSocket.recv(1024)
    print (message.decode())

printMessageFromServer()

request = input('... Enter HELO: <domain-name> ... \n')
if (request[:4] == 'HELO'):
    clientSocket.send(request.encode())
printMessageFromServer()

request = input('... Enter MAIL FROM: <mail-address-of-sender> ... \n')
if (request[:9] == 'MAIL FROM'):
    clientSocket.send(request.encode())
printMessageFromServer()


request = input('... Enter RCPT TO: <mail-address-of-recipient> ... \n')
if (request[:7] == 'RCPT TO'):
    clientSocket.send(request.encode())
printMessageFromServer()

request = input('... Enter DATA ... \n')
if (request[:4] == 'DATA'):
    clientSocket.send(request.encode())
printMessageFromServer()

print('... Enter the contents of the message ...')
delim = ""
request = ""
data = []
while True:
    line = input()
    if line[-1:] == '.':
        break;
    else:
        data.append(line)

request = '\n.'.join(data)

print (request)
clientSocket.send(request)
printMessageFromServer()

