#!/usr/bin/env python3
# Créditos: Foundations of Python Network Programming, Third Edition (https://github.com/brandon-rhodes/fopnp)
# Consulta DNS básica

import argparse, dns.resolver

'''
Obtém os principais registros de DNS de um dado domínio
'''
def lookup(nome):
    for tbusca in 'A', 'AAAA', 'CNAME', 'MX', 'NS':
        resposta = dns.resolver.resolve(nome, tbusca, raise_on_no_answer=False)
        if resposta.rrset is not None:
            print(resposta.rrset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resolve um nome usando DNS')
    parser.add_argument('nome', help='nome ao qual você deseja buscar no DNS')
    lookup(parser.parse_args().nome)
