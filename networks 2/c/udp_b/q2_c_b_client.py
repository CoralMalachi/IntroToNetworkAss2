import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_ip = '10.0.2.15'
dest_port = 12345

BUFSIZE = 1024
msg = "A"

for i in xrange(11): 
    s.sendto(msg, (dest_ip, dest_port))
    s.sendto(msg, (dest_ip, dest_port))
    time.sleep(2)

s.sendto("*FINISH*", (dest_ip,dest_port))


data, sender_info = s.recvfrom(BUFSIZE)
print "Server sent: ", data

s.close()
