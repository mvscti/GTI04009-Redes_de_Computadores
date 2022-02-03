import socket

#endereço de boradcast
BROADCAST='' #endereço de broadcast
PORTA=10000 #porta ao qual o servidor estará "escutando"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria um UDP/IP socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
msg = input('Para sair use CTRL+X e pressione enter\n')
while msg != '\x18':
	#envia mensagem
	s.sendto(msg.encode('utf8') , (BROADCAST, PORTA))
	msg = input()
print('Fechando socket....')
s.close()