import socket

from settings import HOST, PORT

host = HOST
port = PORT

try:
    sock = socket.socket()
    sock.bind((host, port))
    print('Server started')
except KeyboardInterrupt:
    print('Server closed')