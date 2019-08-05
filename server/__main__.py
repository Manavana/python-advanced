import socket

from settings import HOST, PORT

host = HOST
port = PORT

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    print('Server started')

    while True:
        client, address = sock.accept()
        print(f'Client with address { address } was detected')
except KeyboardInterrupt:
    print('Server closed')