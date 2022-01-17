import argparse, socket, sys

#endereço de boradcast
broadcast='192.168.35.31'

#porta ao qual o servidor estará "escutando"
porta=10000

#cria um UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Envie para todo mundo
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 

msg = input('Para sair use CTRL+X e pressione enter\n')
while msg != '\x18':
	#envia os dados
    #msg = msg.encode('ascii') #codifica para ASCII
	s.sendto(msg.encode('ascii') , ('192.168.35.31', porta))
	
	msg = input()
	
print('closing socket')
s.close()