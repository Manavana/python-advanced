import json
import socket
import yaml
import argparse

from settings import HOST, PORT, BUFFERSIZE, ENCODIND

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODIND

# описываем парсер аргументов
parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)
args = parser.parse_args()

# если внутри аргументов args обнаружится config, то произойдет определение файла конфигураций, извлечение его значений
# и переопределение констант
if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)

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