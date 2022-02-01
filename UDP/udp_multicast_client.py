import socket

MULTICAST_GROUP = '224.1.1.1'
PORTA = 55555
MULTICAST_TTL = 20 #Time to Live - número máximo de saltos até que o pacote possa ser descartado
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.IPPROTO_IP, 
                socket.IP_MULTICAST_TTL, 
                MULTICAST_TTL)
msg = input('Para sair use CTRL+X e pressione enter\n')
while msg != '\x18':
	#envia mensagem
	s.sendto(msg.encode('utf8') ,(MULTICAST_GROUP, PORTA))
	msg = input()
print('Fechando socket....')