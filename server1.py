#this file implements server1
import socket

m_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define connection info
PORT = 12345
IP = '0.0.0.0'

m_server.bind((IP, PORT))

# server listens to the client requests
m_server.listen(5)
while True:
    client_socket, client_address = m_server.accept()
    print 'Connection from: ', client_address

    # get the data from the client
    client_data = client_socket.recv(1024)
    while not client_data == '':
        print 'Received: ', client_data
        # send message to the client (same message we got with uppercase)
        client_socket.send(client_data.upper())
        # get message from the client
        client_data = client_socket.recv(1024)
    print 'Client disconnected'
    # close client socket
client_socket.close()
