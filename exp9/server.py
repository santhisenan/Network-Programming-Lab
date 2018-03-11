# server for chat room using tcp

import socket 
import select # to provide accessto the select() and poll() functions available in most operating systems
import sys # system specific parameters and function
from thread import * # provides low-level primitives for working with multiple threads

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server socket in tcp
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 


IP_ADDR = "127.0.0.1"
PORT = 8000 
server.bind((IP_ADDR, PORT))

server.listen(100)

clients = [] # list of clients


def remove(connection):
    if connection in clients:
        clients.remove(connection)

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
                break
            except:
                client.close()
                
                remove(client)


def clientThread(conn, addr):
    conn.sendto("Hi there, ~from server..!", addr)

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print "[" + addr[0] + "]: "+ str(addr[1]) + " => "+ message
                broadcastMessage = "<[" + addr[0] + "] :" + str(addr[1]) + "> => "+ message
                broadcast(broadcastMessage, conn)
            else: 
                remove(conn)
        except: 
            continue


while True:
    conn, addr = server.accept()
    clients.append(conn)
    print addr[0] + ":"+ str(addr[1])+ " connected"
    start_new_thread(clientThread,(conn,addr)) 
conn.close()
server.close()                               





