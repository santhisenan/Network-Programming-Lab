# client for chat room
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


IP_ADDRESS = "127.0.0.1"
PORT = 8000
server.connect((IP_ADDRESS, PORT))

while True:
    sockets = [sys.stdin, server]
    read_sockets, write_socket, error_socket = select.select(sockets,[],[])
    for sock in read_sockets:
        if sock == server:
            message = sock.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()                    
