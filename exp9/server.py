# server for chat room using tcp

import socket 
import select # to provide accessto the select() and poll() functions available in most operating systems
import sys # system specific parameters and function
from thread import * # provides low-level primitives for working with multiple threads

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server socket in udp
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#check if number of args are 3
if len(sys.argv) != 3:
    print "Number of arguments is not 3."
    # print "Usage: script, IP Address, Port Number"
    # exit()

IP_ADDR = "127.0.0.1" # first arg
PORT = 8000 # second arg
server.bind((IP_ADDR, PORT))

server.listen(100)

clients = [] # list of clients

def clientThread(conn, addr):
    conn.send("Hi there!")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print "[" + addr[0] + "] "+ message
                brodcastMessage = "[" + addr[0] + "] "+ message
                broadcast(brodcastMessage, conn)
            else: 
                remove(conn)
        except: 
            continue
def broadcast(message, connection):
    for client in clients:
        if(client != connection):
            try:
                client.send(message)
            except:
                client.close()

                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print addr[0] + " connected"
    start_new_thread(clientThread,(conn,addr)) 
conn.close()
server.close()                               





