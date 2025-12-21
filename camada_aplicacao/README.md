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
O  Sistema de Nomes de Domínio, mais conhecido pela sigla DNS (em inglês), é um protocolo da camada de aplicação que permite com que seres humanos possam se comunicar com qualquer <em>host</em> sem a necessidade de memorizar ou saber seu endereço IP. Ao invés disso, um grande sistema hierárquico e distribuído, permite que seja feita a "traduação" de um endereço IP para um domínio (alfanumérico), muito mais fácil de ser memorizado do que um endereço IP (imagine se o endereço IP de um <em>host</em> for um endereço na sexta versão, com 128 bits). O melhor termo que define o papel deste protocolo seria **resolução** de nomes, ao invés de tradução. Por padrão, o DNS utiliza o protocolo [UDP](https://github.com/mvscti/GTI04009-Redes_de_Computadores/tree/main/camada_transporte) na porta número 53. O DNS trabalha em uma arquitetura do tipo cliente-servidor.

Na figura a seguir, podemos compreender melhor como funciona a hierarquia do DNS:

![dns-hierarquia](https://www.inetdaemon.com/img/dns-hierarchy.gif)


* Servidores-raiz (root-servers) : Os [treze servidores-raiz](https://root-servers.org/) são servidores de nome para a chamada zona raiz do DNS. Na verdade, existem 13 servidores-raiz lógicos, mas existem cópias desses (algumas milhares), espalhadas pelo Planeta para promover escalabilidade. Essa dispersão ocorre estrategicamente pelo mundo e se todos eles estiverem indisponíveis, podemos dizer que o DNS falhará em escala global. A função deles é responder às requisições de registros da zona raiz e também a outras requisições, retornando uma lista dos servidores de nome designados para o domínio de topo apropriado. Eles estão "na linha de frente" na tarefa de resolução de nomes para endereços IP.
* Servidores de domínio de topo (top-level domain ou TDL): um domínio (ex.: dominio.com.br) é lido por nós, humanos, da esquerda para direita. Mas para os computadores, a resolução de um domínio começa da direita para esquerda, ou seja, de trás para frente (no exemplo anterior, a ordem seria br.com.dominio). Cada domínio é separado por um ponto. O que se encontra mais à direita, é o [domínio de topo](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains) (.gov; .br; .edu; etc..). Cada servidor de domínio de topo conhece os endereços dos servidores autoritativos que pertencem aquele domínio de topo, ou o endereço de algum servidor DNS intermediário que conhece um servidor autoritativo. Nesta categoria, entram também os domínios orientados à países (<em>Country Code Top Level Domains</em>), como por exemplo, [.br](https://registro.br) para o Brasil, .ar para Argentina, dentre outros.
* Servidores com autoridade: Possuem os registros originais que associam aquele domínio a seu endereço de IP. Por exemplo, o domínio root-server.org tem como TDL  ```.org``` e como servidor autoritativo ```root-server```. Cabe ao servidor autoritativo determinar qual o endereço IP do domínio ```root-server``` e dos demais domínios que antecedem ao ```root-server``` (por exemplo, o ```www``` ou ```ftp``` ou qualquer que seja(m) o(s) outro(s)). Cada domínio que antecede ao ```root-server``` tem de ter seu endereço IP registrado pelo servidor autoritativo.

Existem algumas ferramentas que permitem explorar melhor um determinado domínio na Internet. Algumas delas podem ser instaladas no seu sistema operacional e existem diversas outras online, como o [nslookup.io](https://www.nslookup.io/) ou o [dig](https://toolbox.googleapps.com/apps/dig/). 

Para saber mais sobre DNS e principalmemte, como funcionam os registros DNS, leia mais neste [artigo](https://pt.wikipedia.org/wiki/Sistema_de_Nomes_de_Dom%C3%ADnio).

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

## Agente do Usuário
Um importante fator presente na camada de aplicação, que visa facilitar a utilização dos protocolos pelos usuários, são os **agentes do usuário**. Resumidamente, um agente do usuário é um software (dotado de interface gráfica ou baseada em comandos) que permite com que ocorra a interação entre o usuário e um determinado protocolo. Na arquitetura cliente-servidor, o agente do usuário é também conhecido como cliente ou software cliente. Exemplos de agentes do usuário, para os mais diversos protocolos da camada de aplicação e não limitados somente a estes:
* Navegador (ou <em>browser</em>), para os protocolos HTTP, HTTPS e FTP
* Webmail (cliente de email na web), para os protocolos SMTP e POP3. Ex.: Gmail, Microsoft Outlook, Yahoo! Mail, etc
* Cliente de email, para os protocolos SMTP e POP3. Ex.: Mozilla Thunderbird
* Terminais do Windows e Linux, para diversos procotolos, como FTP, SSH, Telnet, SCP, etc.
* BitTorrent (ou torrrent), para compartilhamento de arquivos em uma arquitetura P2P. Ex.: BitTorrent (software cliente), uTorrent, etc.

Um exemplo interessante é simular um agente do usuário para o protocolo HTTP, no caso, um <em>browser</em>. Quando acessamos qualquer página na web, costumamos não perceber que o navegador é um facilitador do processo de acesso (como deveria ser qualquer agente do usuário), bastando apenas informar a URL da página e se tudo ocorrer bem, podemos visualizar o seu conteúdo. No entanto, normalmente não temos a noção do que ocorre nos "bastidores" dessa requisição. Qualquer navegador, deve seguir os preceitos do protocolo HTTP (mais a frente falaremos sobre isso) para que seus utilizadores possam visualizar as páginas desejadas. Quando informamos a URL de uma página na barra de endereços do navegador, o mesmo utiliza as informações que inserimos para fazer uma requisição a um servidor HTTP (lembre-se que o HTTP funciona, por padrão, na porta TCP, número 80), utilizando os <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods" target="_blank">preceitos do protocolo</a>, algum de seus verbos ou métodos.

Existem diversas formas de utilizar um cliente web que não seja um navegador, mas uma forma interessante é utilizar o já conhecido comando ```nc```, do Linux. Neste exemplo, vamos fazer uma requisição ao servidor HTTP da Google:
```echo -e "GET / HTTP/1.1\r \nHost: www.google.com.br\r\n" | nc www.google.com.br 80```

Onde:
* ``` GET / HTTP/1.1``` significa que a requisição foi feita utilizando o método ```GET```, requisitando o recurso ```/``` (normalmente, é a página padrão, ou ```index.html```) e ```HTTP/1.1``` significa que a requisição é feita pela versão ```1.1``` do protocolo
* ```Host: www.google.com``` é o domínio ou endereço IP que o servidor atende
* O comanando ```echo``` acima funciona como se fosse um valor digitado pelo usuário e "exportado" para o comando ```nc www.google.com.br 80```, onde ```80``` é a porta a qual o servidor web responde (como mencionando anteriormente, é a porta padrão em que os servidores HTTP respondem)

Se tudo ocorrer bem, você verá o conteúdo HTML da página inicial da Google e também o cabeçalho da resposta. Analise o cabeçalho da resposta, e saberá o <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status" target="_blank">status da requisição</a>, a data em que requisição ocorreu, dentre outras informações (é possível descobrir até qual é o software que o servidor web utiliza, normalmente Apache ou Nginx. 

Outra ferramenta interessante para esta tarefa é o cURL (disponível também no Windows, desde a versão 10). Exemplos:
##### Recuperando o apenas o cabeçalho da resposta
```curl -I https://google.com.br```

##### Recuperando toda a resposta
```curl https://reqbin.com/echo```

### Simulando um agente do usuário para o protocolo SMTP
O protocolo SMTP (do inglês, <em>Simple Mail Transfer Protocol</em> - Protocolo Transferência de Email Simples) é um dos mais antigos protocolos da camada de aplicação da pilha TCP/IP e é o principal protocolo para envio de emails até os dias de hoje. Um servidor SMTP responde, por padrão, <strong>na porta TCP, número 25</strong>. O principal protocolo para <strong>recebimento de emails</strong> é o <a href="http://deptal.estgp.pt:9090/cisco/ccna1/course/module10/10.1.1.4/10.1.1.4.html" target="_blank">POP3</a>, que, por padrão, responde na porta TCP, número 110. E, sim! O serviço de email pode conter dois protocolos: um para envio e outro para recebimento.

Quando você acessa seu email através de um navegador, você está utilizando um **webmail**, que de tão comum que é nos dias atuais, se tornou mais popularmente chamado apenas de email. Mas, como você já descobriu, o email é um serviço muito mais antigo do que a própria web. O que seu provedor de webmail faz é disponibilizar a você uma interface gráfica que facilita a sua interação com os protocolos SMTP e POP3 (ou seja, seu webmail é um agente do usuário para emails). Tanto é, que se você quiser enviar emails da forma como o protocolo SMTP realmente trabalha, em teoria, você poderia fazê-lo (os principais provedores de email atuais adicionam etapas de segurança, que tornam este processo um pouco mais burocrático). Conforme você pode ver na figura a seguir, um email é enviado utilizando todos os trâmites preconizados pelo protocolo SMTP, onde ```S``` significa uma resposta do servidor, ```C``` é uma mensagem do cliente e os números que aparecem são [códigos numéricos de resposta](http://penta2.ufrgs.br/rc952/trab1/smtpcodi.html) (parecido com o que temos no protocolo HTTP):

![smtp](https://www.smtp2go.com/wp-content/uploads/2017/02/Screenshot-9-763x500.png)

Ou seja, o que o webmail faz para você é justamente utilizar os processos necessários do protocolo SMTP para que você tenha uma interface simples, intuitiva e objetiva (espera-se) para enviar seus emails. Existem outros agentes do usuário para o protocolo SMTP e POP3, como o Mozilla Thunderbird, mencionado anteriormente. A diferença desses em relação ao uso de webmails, é que esses clientes de email devem ser instalados em seu dispositivo.

Você mesmo (a) pode simular um agente do usuário (sem interface gráfica) no seu dispositivo, usando o telnet:
 * ```telnet <DOMÍNIO> <PORTA> ```, onde a porta padrão, conforme mencionado anteriormente, é a 25. 
 
 Se tudo ocorrer bem, você deverá conseguir enviar um email utilizando puramente o protocolo SMTP.

Conforme mencionado anteriormente, por razões de segurança, a maior parte dos grandes provedores de email atualmente disponíveis adicionaram passos extra para se autenticar nestes servidores (como autenticação em duas etapas) e tornou mais burocática a tarefa de conseguir enviar emails utilizando uma interface de comandos, como o telnet. Ainda assim, se você quiser apenas entender melhor como funciona o protocolo, como age um servidor SMTP (e também um agente do usuário), existem algumas soluções didáticas para isso, como o [Devnull SMTP Fake Server](http://www.aboutmyip.com/AboutMyXApp/DevNullSmtp.jsp). Trata-se de um servidor SMTP falso (não envia emails), que tem por objetivo demonstrar, de forma didática, um servidor SMTP atuando, sem ser necessário criar emails, configurar ou coisas do tipo. Não é necesária a instalação, mas é preciso ter uma máquina virtual Java instalada em sua máquina, na versão 1.4 ou superior. Depois de baixar o "servidor" (o código se encontra [neste respositório](DevNullSmtp.jar)) e com a máquina virtual Java instalada e configurada em sua máquina, basta executar o seguinte comando no terminal do seu Sistema Operacional:
* ```java -jar DevNullSmtp.jar```

Se você optar por "estartar" o servidor na porta padrão de um servidor SMTP (TCP, número 25), possivelmente precisará de privilégios administrativos do seu sistema. Caso isso ocorra, no Windows, abra o terminal para executar o comando acima como administrador e se estiver utlizando Linux, pode fazer da seguinte forma:
* ```sudo java -jar DevNullSmtp.jar```

Enquanto o servidor estiver em execução, você pode utilizar o telnet para estudar o protocolo. Há também um [código](smtp.py) no repositório, em Python, que simula um cliente SMTP, utilizando a biblioteca ```smtplib```. Com este script, você pode automatizar suas aplicações pare enviarem emails (a maior parte das linguagens de programação multipropósito, como Python, têm bibliotecas que permitem envio de emails). Para executar o script, basta digital o seguinte comando, no terminal:
* ```python3 smtp.py <DOMÍNIO> <ENDRECO_REMETENTE> <ENDERECO_DESTINATARIO>```

Uma outra abordagem prática para conhecer o protocolo (e também mais moderna), é usar um servidor de email para testes. Neste caso, vamos utilizar o MailHog. Para executar, é necessário ter o docker instalado e executar o seguinte comando, dentro deste diretório:

* ```docker compose up```
