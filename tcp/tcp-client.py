import socket
import binascii

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("remote", (HOST, PORT), "local", s.getsockname())
request = bytearray([0x31, 0x32, 0x33, 0x34])
s.sendall(request)
response = s.recv(1024)
print('Received', binascii.hexlify(response))
