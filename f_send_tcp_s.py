
import socket
import sys

port = 2000

print("Waiting for Connection")

msg = c_sock.recv(1024)
print(msg.decode())

with open("./dummy/"+ filename, 'rb')as f:
    c_sock.sendfile(f, 0)

print('Sending complete')
c_sock.close