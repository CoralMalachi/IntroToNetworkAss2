import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_ip = '127.0.1.1'
dest_port = 12345

BUFSIZE = 1024
msg = "A"*15000

s.sendto(msg, (dest_ip,dest_port))

data, sender_info = s.recvfrom(BUFSIZE)
print "Server sent: ", data

s.close()
