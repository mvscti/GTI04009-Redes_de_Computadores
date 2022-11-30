[Retornar a Tabela de Conteúdos](./)
# Camada de Transporte

No modelo TCP/IP, a camada de transporte é encarregada pela transmissão de dados entre máquinas. O serviço que a camada de transporte oferece à camada situada acima dela (camada de aplicação) é um conjunto de procedimentos e funções para acesso ao sistema de comunicação, de modo a permitir a criação e a utilização de aplicações de forma independente da implementação da rede. Dois protocolos se destacam bastante nesta camada, o TCP e o UDP.

### Transmission Control Protocol (TCP)

Protocolo confiável (garante a entrega dos pacotes), portanto orientado a conexão.Em suma, ele refaz o envio dos datagramas em caso de erros, mantém a organização dos pacotes (nem sempre chegam na ordem correta) e também garante que os dados não cheguem duplicados. Podemos dizer que o TCP é o sustentáculo da Internet.
Para garantir a entrega confiável de pacotes, basicamente, o TCP identifica cada pacote com uma espécie de etiqueta, contendo um número sequencial (normalmente aleatório), onde cada extremidade é capaz de verificar e ordenar os dados na sequência correta.
O processo de estabelecimento de uma conexão TCP é baseado no processo de "aperto triplo de mão" (<em>three-way-handshake</em>), conforme pode ser visto na figura abaixo:
![three-way-handshake](https://upload.wikimedia.org/wikipedia/commons/8/8a/Tcp-handshake.png)
- SYN (<em>Synchronize</em>)- "Quero me comunicar com você, aqui está o número sequencial do pacote com o qual começarei"
- SYN-ACK - "Certo, aqui está o número sequencial inicial usarei na minha direção"
- ACK (<em>Acknowledgement)- "Certo!"
Outros três ou quatro pacotes são necessários para finalizar uma conexão (FIN, FIN-ACK, ACK).

### User Datagram Protocol (UDP)

Diferente do TCP, o UDP é considerado um protocolo não confiável, ou seja, não há a garantia de entrega dos dados. Também não há a ordenação dos pacotes e nem controle de fluxo. O UDP é mais utilizado em aplicações que demandam de simplicidade ou fluxo de dados de tempo real (como em <em>streamings</em>). Aplicações que encaixam num modelo de pergunta-resposta (como o DNS, que será visto em outra oportunidade) são beneficiadas pelo uso do UDP.
### Portas TCP e UDP
Ambos os protocolos TCP e UDP utilizam o conceito de portas que, resumidamente, permitem com que mais de uma aplicação possa operar sob um mesmo endereço IP. Uma analogia interessante é a de um prédio. Neste caso, cada <em>host</em> é um prédio. O endereço deste prédio seria o seu endereço IP e o complemento (as portas TCP ou UDP), são os números dos apartamentos. Assim como neste exemplo, as portas (números dos apartamentos), podem até serem repetidas, mas nunca para um mesmo prédio (pode haver o apartamento número 21 no prédio A e também no prédio B, mas nunca dois apartamentos com número 21 para um mesmo prédio). São utilizados 2 bytes para representar número de portas (tanto para o TCP quanto UDP), sendo possível representar 65.536 portas distintas para cada protocolo. Algumas portas já são conhecidas para serviços famosos na Internet, como por exemplo:
* Porta 21 TCP - FTP
* Porta 53 UDP - DNS
* Porta 80 TCP - HTTP
* Porta 443 TCP - HTTPS
As portas compreendidas entre 0 e 1023 são conhecidas por <em>well-known ports</em>. São aquelas destinadas aos serviços mais comuns na Internet, como email, web, transferência de arquivos, etc. As demais portas podem estar livres e podem ser utilizadas por outras aplicações.

# Práticas com TCP e UDP

Neste diretório, se encontram os códigos utilizados nas práticas sobre o protocolo TCP e UDP. Todos os <em>scritps</em> foram escritos em Python 3. A relação segue abaixo:
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

Cada script visa explorar aspectos distintos no emprego dos protocolos TCP e UDP para transmissão de pacotes em uma rede de dados. Ou seja, os scripts demonstram cenários onde um serviço sem confirmação de entrega, como o UDP, poderia ser aplicado e outros onde o TCP seria a melhor solução.

### udp_local e udp_remoto <a href="https://github.com/brandon-rhodes/fopnp" target="_blank">(Créditos: Foundations of Python Network Programming)</a>

Permitem, através de uma forma básica, a comunicação através de [sockets](https://blog.pantuza.com/artigos/o-que-sao-e-como-funcionam-os-sockets) UDP. A versão local permite executar um servidor que responde apenas a requisições na interface de <i>loopback</i> e a remota, a qualquer requisição UDP vinda de uma rede local ou até mesmo através da Internet. Para execução da versão local:
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

Servidor simples que retransmite ao cliente todas as mensagens que recebe. Pode se comportar como um servidor UDP e TCP. Um software de captura de pacotes, como o <a href="https://www.wireshark.org/" target="_blank">wireshark</a>, pode ser útil para visualizar a diferença entre ambos os protocolos. O script não acompanha um cliente. Neste caso, o utilitário Netcat, do Linux, permite enviar pacotes TCP e UDP e é um exemplo que pode ser empregado para funcionar como cliente. Para executar o script:

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

### udp_broadcast (cliente e servidor)
Demonstra o encaminhamento de um pacote a todos destinatários, simultanemanete, em uma subrede local. É necessário informar, no código, a porta UDP a qual servidor escuta (no cliente e no servidor). 
![comunicação_broadcast](https://upload.wikimedia.org/wikipedia/commons/d/dc/Broadcast.svg)

### sender_file_tcp_udp
Permite enviar arquivos entre dois hosts e demonstra como um serviço sem confirmação, como o UDP, pode comprometer a entrega. É possível executar o código utlizando TCP ou UDP (emissor e receptor). Para executar:

```
$ python3 sender_file_tcp_udp.py <TIPO> -p <PORTA> -host <HOST> -file <NOME_DO_ARQUIVO>
```
Onde:
*  `<TIPO>`: pode ser `receiver-tcp`, `receiver-udp`, `sender-tcp` e`sender-udp`
* `<PORTA>`: (opcional) é a porta a qual o receptor do arquivo está "escutando" (padrão 1060)
* `<HOST>`: endereço IP do receptor
* `<NOME_DO_ARQUIVO>`: Nome do arquivo a ser enviado ou recebido. Por exemplo `landscape.jpg` (presente no diretório).

É indicado enviar arquivos de tamanho superior a 2MB para ter mais chances de perceber os problemas no recebimento do arquivo ao utilizar UDP para este fim.

## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3``
- ``Visual Studio Code``
