
import socketserver
import binascii


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def setup(self):
        # 客户端与服务器建立连接
        print('connected by %s' % (self.client_address, ))

    def finish(self):
        # 客户端与服务器连接被关闭
        print('closing', self.client_address)

    def handle(self):
        data = self.request.recv(1024)
        if data:
            print('received "%s" from %s' % (binascii.hexlify(data), self.client_address))
            self.request.sendall(data)


HOST = ''
PORT = 50007
if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print('starting up on %s port %s' % (HOST, PORT))
        server.serve_forever()

