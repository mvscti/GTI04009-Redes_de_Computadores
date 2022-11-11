#!/usr/bin/env python3
'''
O presente código realiza o envio de uma mensagem para ser checada por um receptor,
utilizando a checagem cíclica de redundância (CRC).
Créditos: https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
'''
import socket		

def xor(a, b):

	
	result = []

	
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)



def mod2div(divident, divisor):

	
	pick = len(divisor)

	tmp = divident[0 : pick]

	while pick < len(divident):

		if tmp[0] == '1':

			
			tmp = xor(divisor, tmp) + divident[pick]

		else: 
			tmp = xor('0'*pick, tmp) + divident[pick]

		pick += 1

	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword

def encodeData(data, key):

	l_key = len(key)
	appended_data = data + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)
	codeword = data + remainder
	return codeword
	
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
porta = 12345		
ip_adress='' #endereço IP do receptor
input_string = input("Digite o dado que você quer enviar->")
data =(''.join(format(ord(x), 'b') for x in input_string))
print("Dado em formato binário :",data)
key = "1001" #utiliza uma chave polinomial de grau 3 (x³+x^0)

ans = encodeData(data,key)
print("Dado decodificado a ser enviado para o servidor em formato binário :",ans)
s.sendto(ans.encode(),(ip_adress, porta))


# recebe dado do recpetor
print("Feedback recebido pelo servidor :",s.recv(65535).decode())

#fecha conexão
s.close()
