import socket, struct

MAX_BYTES = 65535
PORTA  = 55555
MULTICAST_GROUP = '224.1.1.1'
HOST_ADDR    =  socket.gethostbyname(socket.gethostname()) #recebe o endereço IP do adaptador
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((MULTICAST_GROUP, PORTA))
pacote=struct.pack('4sl', 
                    socket.inet_aton(MULTICAST_GROUP), 
                    socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, 
            socket.IP_ADD_MEMBERSHIP, 
            pacote)
print('Servidor multicast escutando na porta', format(PORTA))
while True:
    message, address = s.recvfrom(MAX_BYTES)
    print(address , ' disse ',message.decode('utf8'))