import socket


try:
    sock = socket.socket()
    print('Server started')
except KeyboardInterrupt:
    print('Server closed')