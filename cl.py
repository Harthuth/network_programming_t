import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address)
while 1:
    time.sleep(1)
    print('현재 시각 : ', sock.recv(1024).decode())