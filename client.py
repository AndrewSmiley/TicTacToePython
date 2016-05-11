__author__ = 'Andrew'
import socket
import sys
from random import randint

import socket
import sys


client_id = randint(1, 101)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 7788)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
#send the client ID
sock.send(str(client_id))
#once we've connected just keep it running...
while True:
    print "waiting for user input: "
    msg = raw_input()
    if msg == 'end':
        break
    sock.send("%s from client %s"% (msg, client_id))

    #Receiving from client
    data = sock.recv(1024)
    #loop till we get data
    while not data:#reply = 'OK...' + data
        data = sock.recv(1024)

    print "From Server: %s" % data
         # connection.send(raw_input())