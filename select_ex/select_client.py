from socket import *
from select import *

sock_list = []
sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
sock_list.append(sock)
sock.connect(('localhost', 2500))

while 1:
    r_sock,w_sock,e_sock = select(sock_list, [],[],0)
    if r_sock:
        for s in r_sock:
            if s == sock:
                msg = sock.recv(1024).decode()
                print("Received: ", msg)
    smsg = input("msg to send: ")
    sock.send(smsg.encode())