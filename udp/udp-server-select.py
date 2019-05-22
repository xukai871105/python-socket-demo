# coding: utf-8
import select
import socket
import binascii

HOST = ''
PORT = 50008

server_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_fd.setblocking(False)

print('starting up on %s port %s' % (HOST, PORT))
server_fd.bind((HOST, PORT))

# 服务端自身也在侦听列表中
inputs = [server_fd]
client_address = None
conn = None

while True:
    readable, writable, exceptional = select.select(inputs, [], [], 1.0)
    for s in readable:
        data, client_address = s.recvfrom(1024)
        if data:
            # 收到客户端数据
            print('received "%s" from %s' % (binascii.hexlify(data), client_address))
            s.sendto(data, client_address)
