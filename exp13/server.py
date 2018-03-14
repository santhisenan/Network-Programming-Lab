import socket
import sys

HOST = '127.0.0.1'
PORT = 3000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

domains = {}
sender_mail_address = ""
recipient_mail_address = ""
while True:
    conn, addr = serverSocket.accept()
    conn.send('220: Service ready'.encode())
    # TODO: send 421 if server is not ready
    request = conn.recv(1024).decode()
    if(request[:4] == 'HELO'):
        domains[conn] = request[5:]
        conn.send('250: Request command completed'.encode())
    
    request = conn.recv(1024).decode()
    if(request[:9] == 'MAIL FROM'):
        sender_mail_address = request[10:]
        conn.send('250: Request command completed'.encode())

    request = conn.recv(1024).decode()
    if(request[:7] == 'RCPT TO'):
        recipient_mail_address = request[10:]
        conn.send('250: Request command completed'.encode())    
  
    request = conn.recv(1024).decode()
    if(request[:4] == 'DATA'):
        conn.send('354: Start mail input'.encode())  


    request = conn.recv(1024).decode()
    email_data = request[:]
    conn.send('250: OK'.encode())  
    

    
    request = conn.recv(1024).decode()
    if(request[:4] == 'QUIT'):
        conn.send('221: Service closing transmission channel'.encode()) 

    conn.close()
    break

serverSocket.close()

