from socket import *
import _thread
HOST = 'localhost'
PORT = 2700
BUFF = 1024

def response(key):
    return '서버 응답 메시지'

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(BUFF)
        print('data:' + repr(data))
        if not data: break
        clientsock.send(response('').encode())
        print('sent:' + repr(response('')))

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET,SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)

    while True:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)
        _thread.start_new_thread(handler, (clientsock,addr))
