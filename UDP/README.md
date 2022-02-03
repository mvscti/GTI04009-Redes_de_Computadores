[Retornar a Tabela de Conteúdos](../#readme)
# Práticas com UDP

Neste diretório, se encontram os códigos utilizados nas práticas sobre o protocolo UDP. Todos os scritps foram escritos em Python 3. A relação segue abaixo:
*   [udp_local](udp_local.py) 
*   [udp_remote](udp_remote.py) 
*   [echoserver_udp_tcp](echoserver_udp_tcp.py)
*   [udp_unicast_server](udp_unicast_client.py)
*   [udp_unicast_client](udp_unicast_client.py)
*   [udp_broadcast_server](udp_broadcast_server.py)
*   [udp_broadcast_client](udp_broadcast_client.py)
*   [udp_multicast_server](udp_multicast_server.py)
*   [udp_multicast_client](udp_multicast_client.py)
*   [sender_file_tcp_udp](sender_file_tcp_udp.py)

## Descrição dos scripts
Cada script visa explorar aspectos distintos no emprego do protocolo UDP para transmissão de pacotes em uma rede de dados. Ou seja, os scripts demonstram cenários onde um serviço sem confirmação de entrega, como o UDP, poderia ser aplicado e outros onde o TCP seria a melhor solução

### udp_local e udp_remoto [(Créditos: Foundations of Python Network Programming](https://github.com/brandon-rhodes/fopnp))

Permitem, através de uma forma básica, a comunicação através de sockets UDP. A versão local permite executar um servidor que responde apenas a requisições na interface de <i>loopback</i> e a remota, a qualquer requisição UDP vinda de uma rede local ou até mesmo através da Internet. Para execução da versão local:
```
$ python3 udp_local.py <TIPO> -p <PORTA> 
```
Onde `<TIPO>` pode ser `client` ou `server` e `<PORTA>` (opcional) é a porta UDP que servidor está "escutando" (padrão 1060).
 
A versão remota pode ser executa como:
```
$ python3 udp_remote.py <TIPO> -p <PORTA> <HOST> 
```
Onde `<TIPO>` pode ser `client` ou `server`, `<PORTA>` (opcional) é a porta UDP que servidor está "escutando" (padrão 1060) e `<HOST>` é o endereço IP ao qual o servidor irá responder.

O servidor na versão local recebe uma mensagem do cliente, determina o tamanho da mensagem recebida (em bytes) e retorna uma mensagem ao cliente. Já na versão remota, o servidor descarta 50% dos pacotes a ele endereçado.

### echo_server_udo_tcp

Servidor simples que retransmite ao cliente todas as mensagens que recebe. Pode se comportar como um servidor UDP e TCP. Quando utilizado um software de captura de pacotes, como o [wireshark](https://www.wireshark.org/), pode ser útil para visualizar a diferença entre ambos os protocolos. Este script não acompanha um cliente. Neste caso, o utilitário netcat, do Linux, netcad permite enviar pacotes TCP e UDP e é um exemplo que pode ser empregado para funcionar como cliente. Para executar o script:

```
$ python3 echoserver_udp_tcp.py <TIPO> -p <PORTA> 
```
Onde `<TIPO>` pode ser `udp` ou `tcp` e `<PORTA>` (opcional) é a porta a qual o servidor está "escutando" (padrão 1060).

### udp_unicast (cliente e servidor)
Demonstra o endereçamento de pacotes feito a um único destinatário. É necessário informar, no código, a porta UDP a qual servidor escuta (no cliente e no servidor). 
![comunicação_unicast](https://upload.wikimedia.org/wikipedia/commons/7/75/Unicast.svg)

### udp_multicast (cliente e servidor)
Demonstra o endereçamento de pacotes feito a múltiplos destinatários, simultaneamente. É necessário informar, no código, a porta UDP a qual servidor escuta (no cliente e no servidor). 
![comunicação_multicast](https://upload.wikimedia.org/wikipedia/commons/3/30/Multicast.svg)

### udp_broacast (cliente e servidor)
Demonstra o endereçamento de um pacote a todos destinatários, simultanemanete, em uma subrede local. É necessário informar, no código, a porta UDP a qual servidor escuta (no cliente e no servidor). 
![comunicação_broadcast](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg)

### sender_file_tcp_udp
Permite enviar arquivos entre dois hosts e demonstra como um serviço sem confirmação de entrega, como o UDP, pode comprometer a entrega. É possível executar o código utlizando TCP ou UDP (emissor e receptor). Para executar:

```
$ python3 sender_file_tcp_udp.py <TIPO> -p <PORTA> -host <HOST> -file <NOME_DO_ARQUIVO>
```
Onde:
*  `<TIPO>`: pode ser `receiver-tcp`, `receiver-udp`, `sender-tcp` e`sender-udp`
* `<PORTA>`: (opcional) é a porta a qual o receptor do arquivo está "escutando" (padrão 1060)
* `<HOST>`: endereço IP do receptor
* `<NOME_DO_ARQUIVO>`: Nome do arquivo a ser enviado ou recebido. Por exemplo `landscape.jpg` (presente no diretório).

É indicado enviar arquivos de tamanho superior a 2MB para ter mais chances de perceber problemas no recebimento do arquivo ao utilizar UDP.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3``
- ``Visual Studio Code``