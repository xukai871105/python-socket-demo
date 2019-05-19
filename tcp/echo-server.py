
import socket
import binascii

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, address = s.accept()
    request = conn.recv(1024)
    print('connected by', repr(address),
          'received ', binascii.hexlify(request))
    if request:
        conn.sendall(request)

