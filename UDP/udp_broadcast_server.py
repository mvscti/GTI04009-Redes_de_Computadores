import socket, traceback

host = ''                               # utiliza todas interfaces
port = 10000
MAX_BYTES = 65535 #quantidade máxima de bytes de uma mensagem
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(MAX_BYTES)
        print(address , " disse ",message.decode('ascii'))
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()