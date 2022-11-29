import socket, traceback
HOST_ADDR = ''                               # utiliza todas as interfaces (é necessário deixar este parâmetro sem valor para funcionar como broadcast)
PORTA = 10000                            #escolher a porta UDP
MAX_BYTES = 65535  #quantidade máxima (em bytes) que a mensagem poderá comportar
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criação do socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((HOST_ADDR, PORTA))
print('Servidor escutando na porta',format(PORTA))
while True:
    try:
        message, address = s.recvfrom(MAX_BYTES)
        print(address , ' disse ',message.decode('utf8'))
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()