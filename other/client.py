from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 8
ADDR = (HOST, PORT)


tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

data = raw_input('>')
print 'shutdown'
tcpCliSock.send(data)

tcpCliSock.shutdown(SHUT_WR)

data = ""
while True:
    try:
        recv_data = tcpCliSock.recv(BUFSIZ)
        if not recv_data:
            break
        data += recv_data
    except Exception as e:
        print e
        break


print data
tcpCliSock.close()
