import socket

port = int(input("Port No : "))
address = ("localhost", port)
BUFSIE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
while 1:
    msg = input("Message to send : ")
    s.send(msg.encode())
    data = s.recv(BUFSIE)
    print("Received message : %s" %data.decode())