__author__ = 'Andrew'
from threading import Thread
from time import sleep
import socket
import sys
'''
    Simple socket server using threads
'''


def serverGame(connection):
    #here we'll get he server id
    data = connection.recv(1024)


    while not data:
        data = connection.recv(1024)
    server_id = data
    f = open("%s" % server_id, "a")
    f.write("Running in  thread %s\n" %server_id)
    while True:
        msg = raw_input()
        connection.send("%s from server %s", msg, server_id)
        f.write("%s from server %s\n", msg, server_id)
        data = connection.recv(1024)
        while not data:
            data = connection.recv(1024)
        print "From server: %s" %data
        f.write("From server: %s\n" %data)






HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 7788 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread = Thread(target = serverGame, args =[conn])
    thread.start()
    # thread.join()
    print "thread finished...exiting"


s.close()