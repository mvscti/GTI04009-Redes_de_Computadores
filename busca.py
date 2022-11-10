#!/usr/bin/env python3
''' Obtém o endereço IP de um host através de seu domínio. 
Créditos: Foundations of Python Network Programming, Third Edition/https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/getname.py
'''
import socket

if __name__ == '__main__':
    hostname = 'ifsudestemg.edu.br'
    addr = socket.gethostbyname(hostname)
    print('O endereço IP de {} é {}'.format(hostname, addr))
