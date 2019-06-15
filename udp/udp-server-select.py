# coding: utf-8
import select
import socket
import binascii

HOST = ''
PORT = 50018

server_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_fd.setblocking(False)

server_fd.bind((HOST, PORT))
print('starting up on %s port %s' % (HOST, PORT))

# 把服务器套接字加入到输入列表中
inputs = [server_fd]
client_address = None
conn = None

while True:
    # readable, writable, exceptional = select.select(inputs, [], [], 1.0)
    readable = select.select(inputs, [], [], 1.0)[0]
    for s in readable:
        data, client_address = s.recvfrom(1024)
        if data:
            # 收到客户端数据
            print('received "%s" from %s' % (binascii.hexlify(data), client_address))
            s.sendto(data, client_address)
