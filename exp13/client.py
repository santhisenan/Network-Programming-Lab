import socket
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3000

clientSocket = socket.socket()
clientSocket.connect((SERVER_HOST, SERVER_PORT))

def printMessageFromServer():        
    message = clientSocket.recv(1024)
    print (message.decode())

print('==========================================')
print ('HELO: <domain-name>')
print('MAIL FROM: <mail-address-of-sender>')
print('RCPT TO: <mail-address-of-recipient>')
print('DATA')
print('the contents of the message')
print('QUIT')
print('==========================================')

print("\n")

printMessageFromServer()

request = input()
if (request[:4] == 'HELO'):
    clientSocket.send(request.encode())
printMessageFromServer()

request = input()
if (request[:9] == 'MAIL FROM'):
    clientSocket.send(request.encode())
printMessageFromServer()


request = input()
if (request[:7] == 'RCPT TO'):
    clientSocket.send(request.encode())
printMessageFromServer()

request = input()
if (request[:4] == 'DATA'):
    clientSocket.send(request.encode())
printMessageFromServer()

print()
delim = ""
request = ""
data = []
while True:
    line = input()
    if line == '.':
        break;
    else:
        data.append(line)

request = '\n'.join(data)
clientSocket.send(request.encode())
printMessageFromServer()

request = input()
if (request[:4] == 'QUIT'):
    clientSocket.send(request.encode())
printMessageFromServer()

clientSocket.close()
