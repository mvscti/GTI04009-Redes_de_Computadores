#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

import argparse, random, socket, sys

MAX_BYTES = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Escutando em', sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print('Fingindo descartar pacote de {}'.format(address))
            continue
        text = data.decode('utf8')
        print('O (a) cliente em {} diz {!r}'.format(address, text))
        message = 'Sua mensagem ocupa {} bytes de tamanho'.format(len(data))
        sock.sendto(message.encode('utf8'), address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    delay = 0.1  # seconds
    text = 'Esta é outra mensagem'
    data = text.encode('utf8')
    while True:
        sock.send(data)
        print('Esperando {} segundos para uma resposta'.format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout as exc:
            delay *= 2  # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('Acho que o servidor está indisponível') from exc
        else:
            break   # we are done, and can stop looping

    print('O servidor disse {!r}'.format(data.decode('utf8')))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Envia e recebe UDP,'
                                     'simula que pacotes são frequentemente descartados')
    parser.add_argument('role', choices=choices, help='qual papel exercerá')
    parser.add_argument('host', help='interface a qual o servidor escuta'
                        'host ao qual o cliente envia rmensagens')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='porta UDP (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)