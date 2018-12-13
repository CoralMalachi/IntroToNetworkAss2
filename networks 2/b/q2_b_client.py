import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '127.0.1.1'
dest_port = 12345
s.connect((dest_ip, dest_port))

BUFSIZE = 1024
msg = "A"

for i in xrange(11):  # sends once, then send it again
    s.send(msg)
    s.send(msg)
    time.sleep(2)

s.send("*FINISH*")
data = s.recv(BUFSIZE)
print "Server sent: ", data

s.close()
