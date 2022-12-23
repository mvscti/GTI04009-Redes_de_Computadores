'''Converte um endereço IP (string) em Binário'''
def ipStr2Bin(endereco):
    endBin = 0
    #"Quebra" os quatro octetos de um endereço IPv4
    for octeto in endereco.split("."):
        endBin = endBin << 8 | int(octeto) #realiza o deslocamento de 8 bits à esquerda (shifting) e acumula os valores
    return endBin

'''Converte um endereço IP (Binário) em String'''
def ipBin2Str(endBin):
    octetosStr = []
    for i in range(4):
        octetosStr.append(str(endBin>>(8*(3-i))&255))
    return ".".join(octetosStr)

endIPStr = "10.0.5.2"
mascaraSubRedeStr = "255.0.0.0"

ipAddressBin = ipStr2Bin(endIPStr)
print(ipAddressBin)
subnetMaskBin = ipStr2Bin(mascaraSubRedeStr)
enderecoRedeBin = ipAddressBin & subnetMaskBin
enderecoBroadcastBin = ipAddressBin | (subnetMaskBin ^ (1<<32)-1)
enderecoRedeStr = ipBin2Str(enderecoRedeBin)
enderecoBroadcastStr = ipBin2Str(enderecoBroadcastBin)

print(f'Endereço de Rede: {enderecoRedeStr}')
print(f'Endereço de Broadcast {enderecoBroadcastStr}')