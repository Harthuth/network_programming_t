#TCP Echo Server Program
from socket import *

port = 2700		# 포트 번호
BUFSIZE = 1024	# 수신 버퍼 사이즈

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))	# 종단점과 소켓 결합. ' 임의 주소'
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept() # 연결소켓, 연결 주소(IP 주소 포트번호) 반환
print('connected by', remotehost, remoteport)
while True:
    try:
        data = conn.recv(BUFSIZE) # 데이터 수신
    except:
        conn.close()
        break
    else:
        if not data:  # ''이면 종료, ''는 False
            break
        print("Received message: ", data.decode())  # 수신 데이터 출력. 바이트형으로 수신됨으로 문자열로 변환#

    try:
        conn.send(data)# 수신 데이터를 되돌려 전송
    except:
        conn.close()
        break
conn.close()