import os.path
import socket

#lets define info of connection:
PORT_NUM = 12345
IP_NUM = '0.0.0.0'

#lets define output
REDIRECT = "HTTP/1.1 301 Moved Permanently"
CONNECTION_IS_DOWN = "Connection: close"
NOT_FOUND = "HTTP/1.1 404 Not Found"
FOUND = "HTTP/1.1 200 OK"

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port_server = PORT_NUM
    ip_server = IP_NUM

    server.bind((ip_server, port_server))
    server.listen(5)

    while True:
        socket_client,client_add = server.accept()
        data_from_client = socket_client.recv(4096)

        print 'Connection from client with address : ',client_add
        print "here"
        print 'data received: ', data_from_client

        data_from_client = data_from_client.split("\r\n")

        #lets check if it is a GET HTTP request
        if "GET" in data_from_client[0]:
            print "hellllllllllllllllllo"
            name_of_file = data_from_client[0].split(" ")[1]
            content_of_file = reading_file(name_of_file)
            #print (content_of_file)


            output_message = ""
            if content_of_file == "redirect":
                output_message = "{}\r\n{}\r\nLocation: /result.html\r\n\r\n".format(REDIRECT, CONNECTION_IS_DOWN)
            elif None == content_of_file:
                output_message = "{}\r\n{}".format(NOT_FOUND, CONNECTION_IS_DOWN)
            else:
                print "hihihi"
                output_message = "{}\r\n{}\r\n\r\n{}".format(FOUND, CONNECTION_IS_DOWN, content_of_file)

            print output_message
            socket_client.send(output_message)
        print 'client connection is off'
        socket_client.close()




def reading_file(file):
    file_path = file
    if file == "/":
        file_path="files/index.html"
    elif file=="/redirect":
        return "redirect"
    else:
        file_path = "files/"+file
    #check if there is no file in directory matches the user request
    if not os.path.isfile(file_path):
        return None

    #dealing with jps files
    if  file_path.endswith(".jpg"):
        file_to_read = open(file_path,"rb")
        print "jpg"
    else:
        file_to_read = open(file_path,"r")
        print "not"

    #reading thr file and save it into var
    content_of_file = file_to_read.read()
    #close the file
    file_to_read.close()
    return content_of_file


if __name__ == '__main__':
    main()






