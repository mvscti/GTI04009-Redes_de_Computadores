[Retornar a Tabela de Conteúdos][https://github.com/mvscti/GTI04009-Redes_de_Computadores#readme]
# Práticas com UDP

Neste diretório, se encontram os códigos utilizados nas práticas sobre o protocolo UDP. Todos os scritps foram escritos em Python 3. A relação segue abaixo:
*   [udp_local](UDP/udp_local.py) (Créditos <a hfref="https://github.com/brandon-rhodes/fopnp" target="_blank">Foundations of Python Network Programming</a>>
*   [udp_remote](UDP/udp_remote.py)  (Créditos <a hfref="https://github.com/brandon-rhodes/fopnp" target="_blank">Foundations of Python Network Programming</a>>
*   [echoserver_udp_tcp](UDP/echoserver_udp_tcp.py)
*   [udp_unicast_server](UDP/udp_unicast_client.py)
*   [udp_unicast_client](UDP/udp_unicast_client.py)
*   [udp_broadcast_server](UDP/udp_broadcast_server.py)
*   [udp_broadcast_client](UDP/udp_broadcast_client.py)
*   [udp_multicast_server](UDP/udp_multicast_server.py)
*   [udp_multicast_client](UDP/udp_multicast_client.py)
*   [sender_file_tcp_udp](UDP/sender_file_tcp_udp.py)

## Descrição dos códigos
Cada script visa explorar aspectos distintos no emprego do protocolo UDP para transmissão de pacotes em uma rede de dados. Ou seja, os scripts demonstram cenários onde um serviço sem confirmação de entrega, como o UDP, poderia ser aplicado e outros onde o TCP seria a melhor solução

### udp_local e udp_remoto

Permitem, através de uma forma básica, a comunicação através de sockets UDP. A versão local permite executar um servidor que responde apenas a requisições na interface de <i>loopback</i> e a remota, a qualquer requisição UDP vinda de uma rede local ou até mesmo através da Internet. Para execução da versão local:
```
$ python3 udp_local.py <TIPO> -p <PORTA> 
```
Onde <i><TIPO></i> pode ser <i>client</> ou <i>server</i> e <i><PORTA></i> é a porta UDP que servidor ou cliente está "escutando" (padrão 1060).
