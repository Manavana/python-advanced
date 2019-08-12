import json
import socket
import yaml
import argparse

from actions import (
    resolve, get_server_actions
)
from protocol import (
    validate_request, make_response, make_400,
    make_404
)
from settings import (
    HOST, PORT, BUFFERSIZE, ENCODIND
)

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
    # устанавливаем сокет-соединение
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(10)
    server_actions = get_server_actions()

    print('Server started')

    while True:
        client, address = sock.accept()
        print(f'Client with address { address } was detected')

        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))

        action_name = request.get('action')

        if validate_request(request):
            controller = resolve(action_name, server_actions)
            if controller:
                try:
                    response = controller(request)
                except Exception as err:
                    print(err)
                    response = make_response(
                        request, 500, 'Internal server error'
                    )
            else:
                print(f'Action with name {action_name} does not exists')
                response = make_404(request)
        else:
            print(f'Request is not valid')
            response = make_400(request)

        s_response = json.dumps(response)
        client.send(s_response.encode(encoding))

        client.close()

except KeyboardInterrupt:
    print('Server closed')