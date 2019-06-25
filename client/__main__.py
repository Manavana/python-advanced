import yaml
import argparse

from settings import ENCODING

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
        encoding = conf.get('encoding', ENCODING)

try:
    print('Client started')
    value = input('Enter data to send: ')
    bvalue = value.encode(encoding)
    print('*' * 15, 'data was send to server', '*' * 15)
    print('*' * 15, 'data was recieved from server', '*' * 15)
    bvalue.decode(encoding)
except KeyboardInterrupt:
    print('Client closed')
