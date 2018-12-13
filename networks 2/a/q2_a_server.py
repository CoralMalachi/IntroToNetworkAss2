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
	#We finish the message with the new message "*FINISH*" to notify the server to stop and check.
    while not data.endswith("*FINISH*"):
        msg = msg + data
        data = client_socket.recv(BUFSIZE)
    msg = (msg + data).replace("*FINISH*", "")  # We neglect "*FINISH*"

	#We check if the message is as we wanted
    if msg == "A" * 15000:
        client_socket.send("B")
    else:
        print "not A*15K..."

    print 'Client disconnected'
    client_socket.close()
