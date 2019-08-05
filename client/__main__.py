import json
import socket
import yaml
import argparse

from settings import HOST, PORT, BUFFERSIZE, ENCODIND

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

# описываем парсер
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
    # устанавливаем сокет-соединение
    sock = socket.socket()
    sock.connect((host, port))

    print('Client started')

    data = input('Enter data to send: ')

    # создали запрос на сервер
    request = json.dump(
        {'data': data}
    )

    sock.send(request.encode(encoding))

    # получение ответа от сервера в виде байтовой строки с последующим декодированием
    b_data = sock.recv(buffersize)
    response = json.loads(
        b_data.decode(encoding)
    )

    print(response)
    sock.close()
except KeyboardInterrupt:
    print('Client closed')
