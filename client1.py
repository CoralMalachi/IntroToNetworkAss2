#this file implements client1
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define connection info
PORT = 12345
IP = '127.0.0.1'

s.connect((IP, PORT))
info = raw_input("Message to send: ")
#when client enter quit connection is off
while not info == 'quit':
    # client sends message to the server
    s.send(info)
    # the client get the response from the server
    data = s.recv(4096)
    #print what server sent
    print "Server sent: ", data
    # get message to the server from the user
    info = raw_input("Message to send: ")
# close client socket
s.close()
