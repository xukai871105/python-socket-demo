# coding: utf-8
import select
import socket
import binascii

HOST = ''
PORT = 50007

server_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_fd.setblocking(False)

print('starting up on %s port %s' % (HOST, PORT))
server_fd.bind((HOST, PORT))
server_fd.listen(5)

# 服务端自身也在侦听列表中
inputs = [server_fd]
client_address = None
conn = None

while True:
    readable, writable, exceptional = select.select(inputs, [], [], 1.0)
    for s in readable:
        if s is server_fd:
            # 有新客户端建立连接
            conn, client_address = s.accept()
            print('connected by', client_address)
            # 将客户端对象也加入到监听的列表中, 当客户端发送消息时select()将触发
            inputs.append(conn)
        else:
            data = s.recv(1024)
            if data:
                # 收到客户端数据
                print('received "%s" from %s' % (binascii.hexlify(data), s.getpeername()))
                s.send(data)
            else:
                # 未收到任何数据，表示客户端关闭连接
                print('closing', client_address)
                # 客户端断开了连接, 将客户端的监听从input列表中移除
                inputs.remove(s)
                s.close()

