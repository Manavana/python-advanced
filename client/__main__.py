from settings import ENCODING


try:
    print('Client started')
    value = input('Enter data to send: ')
    bvalue = value.encode(ENCODING)
    print('*'*15, 'data was send to server', '*'*15)
    print('*'*15, 'data was recieved from server', '*'*15)
    bvalue.decode(ENCODING)
except KeyboardInterrupt:
    print('Client closed')