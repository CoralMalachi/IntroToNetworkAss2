import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '127.0.1.1'
dest_port = 12345
s.connect((dest_ip, dest_port))

BUFSIZE = 1024
msg = "A"*15000

s.send(msg)
s.send("*FINISH*")  # update the server that the message has ended.

data = s.recv(BUFSIZE)
print "Server sent: ", data

s.close()
