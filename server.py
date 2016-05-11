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


    # while not data:
    #     data = connection.recv(1024)
    # server_id = data
    # f = open("%s" % server_id, "a")
    # f.write("Running in  thread %s\n" %server_id)
    f = open("log.log" , "a+")
    while True:
        msg = "Message Recieved"
        # msg = raw_input()
        connection.send("%s"% msg)


        data = connection.recv(1024)
        while not data:
            data = connection.recv(1024)
        f.write("client> %s\n" % data)
        # print "From server: %s" %data

        f.write("server> %s \n" %msg)






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
    serverGame(conn)
    thread = Thread(target = serverGame, args =[conn])
    thread.start()
    thread.join()
    print "thread finished...exiting"


s.close()