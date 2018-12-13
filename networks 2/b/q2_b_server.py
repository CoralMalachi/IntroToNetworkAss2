import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))
server.listen(5)

BUFSIZE = 1024


while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    msg = ""
    data = client_socket.recv(BUFSIZE)
    while not data == "*FINISH*":
        msg = msg + data
        data = client_socket.recv(BUFSIZE)

    if msg == "A" * 22:
        client_socket.send("B")
    else:
        print "not A*22..."

    print 'Client disconnected'
    client_socket.close()
