import socketserver
import binascii


class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        if data:
            print('received "%s" from %s' % (binascii.hexlify(data), self.client_address))
            socket.sendto(data, self.client_address)

HOST = ''
PORT = 50008
if __name__ == "__main__":
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()