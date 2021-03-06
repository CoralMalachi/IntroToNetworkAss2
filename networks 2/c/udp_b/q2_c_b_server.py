import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))

BUFSIZE = 20000


while True:
    msg = ""
    data, sender_info = server.recvfrom(BUFSIZE)
    print 'Connection from: ', sender_info

    while not data == "*FINISH*":
        msg = msg + data
        data, sender_info = server.recvfrom(BUFSIZE)

    if msg == "A" * 22:
        server.sendto("B", sender_info)
    else:
        print "not A*22..."
