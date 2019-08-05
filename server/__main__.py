import json
import socket

from settings import HOST, PORT, BUFFERSIZE, ENCODIND

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODIND

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    print('Server started')

    while True:
        client, address = sock.accept()
        print(f'Client with address { address } was detected')

        b_data = client.recv(buffersize)

        request = json.loads(b_data.decode(encoding))
        response = json.dumps(request)

        client.send(response.encode(encoding))

except KeyboardInterrupt:
    print('Server closed')