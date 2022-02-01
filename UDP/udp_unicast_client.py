import argparse, socket, sys

#endereço de boradcast
SERVER_ADDR='192.168.35.2' #informar endereço IP do servidor
PORTA=25000 #porta ao qual o servidor estará "escutando"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria um UDP/IP socket
msg = input('Para sair use CTRL+X e pressione enter\n')
while msg != '\x18':
	#envia mensagem
	s.sendto(msg.encode('utf8') , (SERVER_ADDR, PORTA))
	msg = input()
print('Fechando socket....')
s.close()