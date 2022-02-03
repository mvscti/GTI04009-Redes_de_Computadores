##Demonstra como podem existir perda de pacotes em serviços sem confirmação, como o UDP.
## É importante executar servidor e cliente em máquinas distintas para poder acompanhar os erros.
## O código executa um servidor (UDP ou TCP) e um cliente (basta informar por parâmetro ao executar o código).
import argparse, socket

def udp_server(port, host='', filename=''):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (host, port)
    udp.bind(orig)
    print('Servidor aguardando requisições no endereço {} e porta {}'.format(host, port))
    udp.settimeout(60)
    with open(filename, 'wb') as f:
         while True:
            try:
                
                data=udp.recv(1024)
                if not data:
                    break
                f.write(data)
            except socket.timeout:
                print('Tempo limite da conexão alcançado')
                break

    f.close()
    udp.close()

def tcp_server(port, host='', filename=''):
    BUFFER_SIZE=1024
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (host, port)
    tcp.bind(orig)
    tcp.listen(5)
    print('Servidor aguardando requisições no endereço {} e porta {}'.format(host, port))
    con, cliente_address=tcp.accept()
    with open(filename, 'wb') as f:
         while True:
            data=con.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
    print('Arquivo recebido. Fechando conexão')  
    tcp.close()    

def tcp_client(port, host, filename):
    try:
        print('Enviando %s ...' % filename)
        f = open(filename, "rb")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        data = f.read() #leitura do arquivo  
        sock.send(data)
    finally:
        f.close()
        sock.close()

def udp_client(port, host, filename):
    BUFFER_SIZE=1024
    try:
        print('Enviando %s ...' % filename)
        f = open(filename, "rb")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((host, port))
        data = f.read(BUFFER_SIZE) #leitura do arquivo
        while(data):
            sock.send(data)
            data=f.read(BUFFER_SIZE)
    finally:
        f.close()
        sock.close()
        
if __name__ == '__main__':
    choices = {'receiver-tcp': tcp_server, 'receiver-udp': udp_server, 'sender-udp': udp_client, 'sender-tcp': tcp_client}
    parser = argparse.ArgumentParser(description='Demonstra possível perda de pacotes utilizando UDP')
    parser.add_argument('tipo', choices=choices, help='emissor do arquivo (TCP ou UDP) ou receptor (TCP ou UDP)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP ou TCP (padrão 1060)')
    parser.add_argument('-host',  help='endereço IP do receptor (para receptor, informar aspas simples)', type=str)
    parser.add_argument('-file',  help='nome do arquivo', type=str)                         
    args = parser.parse_args()
    function = choices[args.tipo]
    function(args.p, args.host, args.file)