import socket, struct, sys

MAX_BYTES = 65535 #Quantidade máxima (em Bytes) que uma mensagem pode ter
PORTA  = 55555

'''Para criar outros grupos, basta 'estartar' outros servidores com outros endereços IP multicast. 
Para saber quais são os endereços IPv4 multicast reservados para redes locais, consulte https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml'''
MULTICAST_GROUP = '224.1.1.1' 

HOST_ADDR    =  socket.gethostbyname(socket.gethostname()) #recebe o endereço IP do adaptador
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Verifica se o Sistema Operacional é Windows ou Linux
if sys.platform == 'win32':
	s.bind(('', PORTA))
else:
      s.bind((MULTICAST_GROUP, PORTA))
pacote=struct.pack('4sl', socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, pacote)
print(f'Servidor multicast escutando na porta {PORTA}. Para encerrar o servidor, é necessário fechar o terminal.')
#Executa um loop 'infinito'
while True:
	mensagem, endereco = s.recvfrom(MAX_BYTES) #aguarda receber mensagens 
	print(f"{address} disse {message.decode('utf8')}") #.decode('utf8'): converte a mensagem recebida no padrão utf-8