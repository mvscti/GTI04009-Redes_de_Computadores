[Retornar a Tabela de Conteúdos](./)
# Camada de Aplicação

Toda as camadas anteriormente estudadas existem para que a camada de aplicação funcione. A camada de aplicação é a camada mais próxima do usuário. No modelo TCP/IP, ela é a quinta camada (e a sétima do modelo OSI).

Desde a criação da Internet, diversos protocolos foram criados para esta camada (e ainda são criados). Alguns destes protocolos foram designados para uso específico e nunca se tornaram padrões. Outros se tornaram obsoletos e alguns perduram até os dias atuais, passando por revisões que os tornem mais adaptados para as necessidades atuais (como é o caso do protocolo HTTP, que veremos mais adiante).

As principais aplicações da Internet, já conhecidas, funcionam nesta camada:
* E-mail
* Páginas da Web
* Transferência de arquivos
* Acesso remoto
* <em>Streaming</em> multimídia
* Mensageiros instantâneos
* etc

Como você deve imaginar, a Internet não faria o menor sentido se esta camada não existisse. Vale destacar que existem três arquiteturas de rede possíveis para esta camada:
1. Cliente-Servidor
2. P2P (<em>peer-to-peer</em>)
3. Híbrida (Cliente-Servidor e P2P)

É uma tarefa difícil descrever todos os protocolos desta camada, haja visto que são muitos e neste momento, algum pode estar sendo criado. Então iremos descrever então alguns dos principais serviços existentes na camada de aplicação.

### DNS - <em>Domain Name System</em>
O  Sistema de Nomes de Domínio, mais conhecido pela sigla DNS (em inglês), é um protocolo da camada de aplicação que permite com que seres humanos possam se comunicar com qualquer <em>host</em> sem a necessidade de memorizar ou saber seu endereço IP. Ao invés disso, um grande sistema hierárquico e distribuído, permite que seja feita a "traduação" de um endereço IP para um domínio (alfanumérico), muito mais fácil de ser memorizado do que um endereço IP (imagine se o endereço IP de um <em>host</em> for um endereço na sexta versão, com 128 bits). O melhor termo que define o papel deste protocolo seria <strong>resolução</strong> de nomes ao invés de tradução. Por padrão, o DNS utiliza o protocolo [UDP](https://github.com/mvscti/GTI04009-Redes_de_Computadores/tree/main/camada_transporte) na porta número 53. O DNS trabalha em uma arquitetura do tipo cliente-servidor.

Na figura a seguir, podemos compreender melhor como funciona a hierarquia do DNS:

![dns-hierarquia](https://www.inetdaemon.com/img/dns-hierarchy.gif)


* Servidores-raiz (root-servers) : Os [treze servidores-raiz](https://root-servers.org/) são servidores de nome para a chamada zona raiz do DNS. Estão espalhados estrategicamente pelo mundo e se todos eles estiverem indisponíveis, podemos dizer que o DNS falhará em escala global. A função deles é responder às requisições de registros da zona raiz e também a outras requisições, retornando uma lista dos servidores de nome designados para o domínio de topo apropriado. Eles estão "na linha de frente" na tarefa de resolução de nomes para endereços IP.
* Servidores de domínio de topo (top-level domain ou TDL): um domínio (ex.: dominio.com.br) é lido por nós, humanos, da direita para esquerda. Mas para os computadores, a resolução de um domínio começa da esquerda para direita. cada domínio é separado por um ponto. O que se encontra mais à direita, é o [domínio de topo](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains) (.gov; .br; .edu; etc..). Cada servidor de domínio de topo conhece os endereços dos servidores autoritativos que pertencem aquele domínio de topo, ou o endereço de algum servidor DNS intermediário que conhece um servidor autoritativo. Nesta categoria, entram também os domínios orientados à países (<em>Country Code Top Level Domains</em>), como por exemplo, [.br](https://registro.br) para o Brasil, .ar para Argentina, dentre outros.
* Servidores com autoridade: Possuem os registros originais que associam aquele domínio a seu endereço de IP. Por exemplo, o domínio root-server.org tem como TDL  ```.org``` e como servidor autoritativo ```root-server```. Cabe ao servidor autoritativo determinar qual o endereço IP do domínio ```root-server``` e dos demais domínios que antecedem ao ```root-server``` (por exemplo, o ```www``` ou ```ftp``` ou qualquer que seja(m) o(s) outro(s)). Cada domínio que antecede ao ```root-server``` tem de ter seu endereço IP registrado pelo servidor autoritativo.

Existem algumas ferramentas que permitem explorar melhor um determinado domínio na Internet. Algumas delas podem ser instaladas no seu sistema operacional e existem diversas outras online, como o [nslookup.io](https://www.nslookup.io/) ou o [dig](https://toolbox.googleapps.com/apps/dig/). 

Para saber mais sobre DNS e principalmemte, como funcionam os registros DNS, leia mais nesta [pesquisa](https://pt.wikipedia.org/wiki/Sistema_de_Nomes_de_Dom%C3%ADnio).

#### Descrição dos scripts de DNS
Há três scripts neste repositório, que facilitam o entendimento de [registros DNS](https://support.google.com/a/answer/48090?hl=pt-BR). Créditos: <a href="https://github.com/brandon-rhodes/fopnp" target="_blank">Foundations of Python Network Programming</a>:
*   [dns_lookup](dns_lookup.py) 
*   [dns_www](dns_www.py) 
*   [dns_email](dns_email.py)
##### dns_lookup
Faz uma leitura de todos os principais registros DNS de um dado domínio (realiza a mesma função do dig e nslookup).
```
$ python3 dns_lookup.py <DOMÍNIO> 
```
Onde `<DOMÍNIO>` é o nome do domínio (sem o WWW).

##### dns_www
Verifica se um dado domínio possui um servidor HTTP (será visto mais adiante), respondendo na porta 80, e informa o seu endereço IP.
```
$ python3 dns_www.py <DOMÍNIO_OU_IP> 
```
Onde `<DOMÍNIO_OU_IP>` é o nome do domínio (sem o WWW) ou o endereço IP do mesmo.

##### dns_email
Verifica se um dado domínio possui registros do [tipo MX](https://support.google.com/a/answer/48090?hl=pt-BR#J) e exibe todos os encontrados
```
$ python3 dns_email.py <DOMÍNIO_OU_IP> 
```
Onde `<DOMÍNIO_OU_IP>` é o nome do domínio (sem o WWW) ou o endereço IP do mesmo.

