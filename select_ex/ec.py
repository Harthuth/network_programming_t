import socket

# port = int(input("Port No: "))
PORT = 2700
HOST = 'localhost'
address = (HOST, PORT)  # 주소는 항상 (ip, port) 튜플
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)  # 서버 연결 요청
while True:
    msg = input("Message to send: ")

    if not msg:
        continue
    try:
        s.send(msg.encode())  # send a message to server
    except:
        print("연결 종료")
        break

    try:  # 데이터 읽기
        data = s.recv(BUFSIZE)  # receive message from server
        if not data:
            print("연결 종료")
            break
        print("Received message: %s" % data.decode())  # 바이트형을 문자열로 변환
    except:  # 연결 종료
        print("연결 종료")
        break
s.close()
