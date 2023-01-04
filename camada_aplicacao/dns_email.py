#!/usr/bin/env python3
# Créditos: Foundations of Python Network Programming, Third Edition (https://github.com/brandon-rhodes/fopnp)
# Procura por um domínio de email (a parte do endereço de email após o '@')
import argparse, dns.resolver

def resolve_hostname(hostname, recuo=''):
    #Imprime um registro A ou AAAA para o 'hostname'; seguido de CNAMEs se necessário
    recuo = recuo + '    '
    resposta = dns.resolver.resolve(hostname, 'A')
    if resposta.rrset is not None:
        for registro in resposta:
            print(recuo, hostname, 'tem um endereço do tipo A', registro.address)
        return
    resposta = dns.resolver.resolve(hostname, 'AAAA')
    if resposta.rrset is not None:
        for registro in resposta:
            print(recuo, hostname, 'tem um endereço do tipo AAAA', registro.address)
        return
    resposta = dns.resolver.resolve(hostname, 'CNAME')
    if resposta.rrset is not None:
        record = resposta[0]
        cname = record.address
        print(recuo, hostname, 'é um alias CNAME para', cname)
        resolve_hostname(cname, recuo)
        return
    print(recuo, 'Erro: nenhum registro A, AAAA, ou CNAME encontrados para', hostname)

def resolve_dominio_email(dominio):
    #Para um endereço de email 'nome@dominio', encontra o endereço IP do seu servidor de domínio
    try:
        resposta = dns.resolver.resolve(dominio, 'MX', raise_on_no_answer=False)
    except dns.resolver.NXDOMAIN:
        print('Erro: Domínio não encontrado', dominio)
        return
    if resposta.rrset is not None:
        dados = sorted(resposta, key=lambda record: record.preference)
        print('Este domínio tem ', len(dados), 'registros MX')
        for d in dados:
            name = d.exchange.to_text(omit_final_dot=True)
            print('Prioridade', d.preference)
            resolve_hostname(name)
    else:
        print('O domínio informado mão possuí registros MX explícitos')
        print('Tentando resolver o domínio como um registro A, AAAA, ou CNAME')
        resolve_hostname(dominio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encontra o endereço IP do servidor de email')
    parser.add_argument('dominio', help='domínio ao qual voc}e deseja enviar email')
    resolve_dominio_email(parser.parse_args().dominio)
