import argparse, socket

def udp(port):
    host=''
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (host, port)
    udp.bind(orig)
    print('Servidor aguardando requisições')
    while True:
        data, cliente_addr = udp.recvfrom(1024)
        texto = data.decode('utf8')
        data= texto.encode('utf8')
        udp.sendto(data,cliente_addr)
    udp.close()

def tcp(port):
    host=''
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (host, port)
    tcp.bind(orig)
    tcp.listen(5)
    print('Servidor aguardando requisições')
    while True:
        cliente, cliente_address=tcp.accept()
        while True:
            msg = cliente.recv(1024).decode('utf8')
            cliente.send(bytes(msg,'utf8'))
        
    tcp.close()    

if __name__ == '__main__':
    choices = {'tcp': tcp, 'udp': udp}
    parser = argparse.ArgumentParser(description='Reenvia mensagem UDP ou TCP')
    parser.add_argument('tipo', choices=choices, help='qual tipo o servidor executará (TCP ou UDP)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP ou TCP (padrão 1060)')
    args = parser.parse_args()
    function = choices[args.tipo]
    function(args.p)
