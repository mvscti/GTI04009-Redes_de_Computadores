#!/usr/bin/env python3
# Créditos: Foundations of Python Network Programming, Third Edition (https://github.com/brandon-rhodes/fopnp)
# Encontra o serviço WWW de um host arbitrário usando getaddrinfo()

import argparse, socket, sys

def conecta(hostname_ou_ip):
    try:
        infolist = socket.getaddrinfo(
            hostname_ou_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
            )
    except socket.gaierror as e:
        print('Falha do nome de serviço:', e.args[1])
        sys.exit(1)

    info = infolist[0]  # por padrão, tenta o primeiro
    socket_args = info[0:3]
    address = info[4]
    s = socket.socket(*socket_args)
    try:
        s.connect(address)
    except socket.error as e:
        print('Falha da rede:', e.args[1])
    else:
        print('Sucesso: host', info[3], 'escuta na porta 80')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tentando conectar na porta 80')
    parser.add_argument('hostname', help='nome do host ao qual você deseja contatar')
    conecta(parser.parse_args().hostname)
