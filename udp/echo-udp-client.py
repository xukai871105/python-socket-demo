import socket
import binascii

HOST = '127.0.0.1'
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print("remote", (HOST, PORT), "local", s.getsockname())

request = bytearray([0x31, 0x32, 0x33, 0x34])
s.sendto(request, (HOST, PORT))
response, server_address = s.recvfrom(1024)
print('received', binascii.hexlify(response), "from", server_address)

