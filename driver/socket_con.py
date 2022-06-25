from socket import socket


class SocketBase(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def recv_mes(self):
        pass

