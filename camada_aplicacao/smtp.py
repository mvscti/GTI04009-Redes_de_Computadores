#!/usr/bin/env python3
#Créditos: Foundations of Python Network Programming, Third Edition (https://github.com/brandon-rhodes/fopnp)
#Envia mensagens utilizando o protocolo SMTP com suporte a criptografia (TLS) - 
# O código não tem suporte a autenticação, bastando consultar a documentação da biblioteca smtplib para aprender
# como auntenticar este script para envio de email  
import sys, smtplib, socket, ssl

message_template = """Para: {}
De: {}
Assunto: Mensagem de Teste de smtp.py
Ola,
Esta e uma mensagem de teste enviada para voce de um script em Python
.
"""

def main():
    if len(sys.argv) < 4:
        name = sys.argv[0]
        print("Sintaxe: {} dompinio endereco_remetente endereco_destinatário [endereco_destinatário...]".format(name))
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template.format(', '.join(toaddrs), fromaddr)
    try:
        connection = smtplib.SMTP(server)
        send_message_securely(connection, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("Sua mensagem pode não ter sido enviada!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Mensagem enviada para {} destinatários {}".format(len(toaddrs), s))
        connection.quit()

def send_message_securely(connection, fromaddr, toaddrs, message):
    code = connection.ehlo()[0]
    uses_esmtp = (200 <= code <= 299)
    if not uses_esmtp:
        code = connection.helo()[0]
        if not (200 <= code <= 299):
            print("Servidor recusou HELO; código:", code)
            sys.exit(1)

    if uses_esmtp and connection.has_extn('starttls'):
        print("Negociando TLS....")
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.set_default_verify_paths()
        context.verify_mode = ssl.CERT_REQUIRED
        connection.starttls(context=context)
        code = connection.ehlo()[0]
        if not (200 <= code <= 299):
            print("Não pode EHLO após STARTTLS")
            sys.exit(5)
        print("Usando conexão TLS.")
    else:
        print("Servidor não suporta TLS; usando conexão normal.")
    
    connection.sendmail(fromaddr, toaddrs, message)

if __name__ == '__main__':
    main()