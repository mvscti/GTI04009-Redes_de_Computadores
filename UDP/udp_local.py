import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria um objeto do tipo socket
    sock.bind(('127.0.0.1', port)) #seu endereço ip local
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf8')
        print('O cliente em {} disse {!r}'.format(address, text))
        text = 'Seu dado ocupa {} bytes'.format(len(data))
        data = text.encode('utf8')
        sock.sendto(data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'A hora é {}'.format(datetime.now())
    data = text.encode('utf8')
    sock.sendto(data, ('127.0.0.1', port))
    print('O  Sistema Operacional me atribui o endereço IP {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode('utf8')
    print('O servidor {} respondeu {!r}'.format(address, text))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Envia e recebe UDP localmente')
    parser.add_argument('role', choices=choices, help='qual papel exercer')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 14000)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)