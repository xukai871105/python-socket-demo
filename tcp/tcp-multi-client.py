from concurrent.futures import ThreadPoolExecutor, wait
import time
import socket
import binascii
import random

HOST = '127.0.0.1'
PORT = 50007


def tcp_client():
    time.sleep(random.randint(1, 5))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("connected remote", (HOST, PORT), "local", s.getsockname())

    time.sleep(random.randint(1, 5))
    request = bytearray([0x31, 0x32, 0x33, 0x34])
    s.sendall(request)
    response = s.recv(1024)
    print("received", binascii.hexlify(response), "local", s.getsockname())

    time.sleep(random.randint(1, 5))
    print("closed local", s.getsockname())
    s.close()


# 创建一个线程池,
executor = ThreadPoolExecutor(max_workers=5)
# 执行多次tcp_client
all_task = [executor.submit(tcp_client) for _ in range(10)]
wait(all_task)
