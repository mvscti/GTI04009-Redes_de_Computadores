#!/usr/bin/env python3
'''
O presente código realiza a checagem cíclica de Redundância (CRC).
Faz então, o papel de receptor de uma mensagem.
Créditos: https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
'''
import socket, traceback
from threading import Thread

'''Realiza uma operação de OU Exclusivo (XOR)'''
def xor(a, b):

	
	resultado = []

	for i in range(1, len(b)):
		if a[i] == b[i]:
			resultado.append('0')
		else:
			resultado.append('1')

	return ''.join(resultado)


'''Realiza uma divisão em módulo 2''' 
def mod2div(divident, divisor):

	# Número de bits que serão submetidos a operação XOR
	pick = len(divisor)

	# Cortando o dividendo para um tamaho apropiado
	tmp = divident[0: pick]

	while pick < len(divident):

		if tmp[0] == '1':

			# substitui o dividendo pelo resultado de uma
			# operação XOR e "puxa" 1 bit para trás
			tmp = xor(divisor, tmp) + divident[pick]

		else: # Se o bit mais a esquerda é '0'
			# Se o bit mais à esquera do dividendo (ou a
			# parte usada em cada etapa) é 0, o passo não pode
			# usar o divisor regular; é necessário  usar um divisor
			# 'todo-0s'.
			tmp = xor('0'*pick, tmp) + divident[pick]

		# incrementa o pedaço para mover à frente
		pick += 1

	
	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword

''' Receptor decodifica mensagem vinda do emissor'''
def decodeData(data, key):

	l_key = len(key)

	# faz operação de append com n-1 zeros ao final do dado
	appended_data = data.decode() + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)

	return remainder

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso")
# reserva uma porta de comunicação em seu computador 
porta = 12345
MAX_BYTES = 65535
s.bind(('', porta))
print("socket usando a porta %s" % (porta))

while True:
	try:
		data, addr = s.recvfrom(MAX_BYTES)
		print('Conexão recebida de ', addr)
		if not data:
			break
		print("Dado recebido codificado em binário:", data.decode())	
		key = "1001"
		ans = decodeData(data, key)
		print("Restante após decodificação->"+ans)

		# Se o restante for todo de bits '0' então não há erro
		temp = "0" * (len(key) - 1)
		if ans == temp:
			s.sendto(("Dado recebido ->"+data.decode() +
					" Nenhum erro encontrado").encode(), addr)
		else:
			s.sendto(("Erro no dado").encode(), addr)

		#t=Thread(target=receive_data, args=(s, data))
		#t.run()
	except(KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()

s.close()
