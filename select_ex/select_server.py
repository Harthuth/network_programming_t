import socket, select
sock_list = []
BUFFER = 1024
port = 2700
s_sock = socket.socket()
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s_sock.bind(('', port))
s_sock.listen(5)
sock_list.append(s_sock)
print("Server waiting on port" + str(port))
while True:
    r_sock, w_sock, e_sock = select.select(sock_list, [],[])
    print(r_sock)
    for s in r_sock:
        if s==s_sock:
            c_sock, addr = s_sock.accept()
            sock_list.append(c_sock)
            print("Client(%s,%s) connectd" % addr)
        else:
            try:
                data = s.recv(BUFFER)
                print("Received: ", data.decode())
                if data:
                    s.send(data)
            except:
                print("Client (%s, %s) is offline "% addr)
                s.close()
                sock_list.remove(s)
        continue
s_sock.close()