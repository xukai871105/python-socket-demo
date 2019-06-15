import socket
import binascii

HOST = '127.0.0.1'
PORT = 50018
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定本地端口
s.bind(('', 50020))

request = bytearray([0x31, 0x32, 0x33, 0x34])
s.sendto(request, (HOST, PORT))
response, server_address = s.recvfrom(1024)
print('received', binascii.hexlify(response), "from", server_address)

