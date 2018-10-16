from socket import *

import time

HOST = ''
PORT = 21567
BUFSIZ = 8
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print 'connected from:', addr

    data = ""
    while True:
        recv_data = tcpCliSock.recv(BUFSIZ)
        print recv_data
        if not recv_data:
            break
        data += recv_data

    time.sleep(60 * 3)
    print 'send data:%s' % data
    tcpCliSock.send(data)

    print 'close connection:', addr
    tcpCliSock.close()
