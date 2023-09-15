import matplotlib.pyplot as plt



# Informe aqui o valor que você gostaria de codificar 
# (Aqui é um ByteString. Portanto, apenas caracteres ASCII são aceitos
ascii_data=b'AB'
print(f'Bitsream: {ascii_data.decode()}')
bitstream = ''.join(format(ord(char), '08b') for char in ascii_data.decode('ascii'))  # Converte o dado em UTF-8 para binário
print(f'Conversão para Binário: {bitstream}')
clock_signal = []
manchester_signal = []

# Convertendo o bitstream em sinal Manchester
for bit in bitstream:
    if bit == '1':
        manchester_signal.extend([1, -1])
    else:
        manchester_signal.extend([-1, 1])
manchester_signal_encoded=''.join(str(e) for e in manchester_signal).replace('-1', '0')       
print(f'Codificação Manchester: {manchester_signal_encoded}')
# Gerando o sinal de clock
clock_period = 1  # Período do clock em unidades de tempo (Assume que o clock é a metade da frequência do bit)
clock_signal = [-1, 1] * (len(bitstream) // clock_period)  

# Criando a figura e os subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

# Plot do sinal de clock
axs[0].step(range(len(clock_signal)), clock_signal, where='post', color='green')
axs[0].set_title('Sinal de Clock')
axs[0].set_ylim([-1.5, 1.5])


# Plot do bitstream
axs[1].step(range(len(bitstream)), [int(bit) for bit in bitstream], where='post', color='blue')
axs[1].set_title(f'Bitstream de {bitstream} ({ascii_data.decode()})')
axs[1].set_ylim([-0.5, 1.5])


# Plot do código Manchester
axs[2].step(range(len(manchester_signal)), manchester_signal, where='post', color='red')
axs[2].set_title('Codificação Manchester')
axs[2].set_ylim([-1.5, 1.5])

# Configurações de formatação
for ax in axs:
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Amplitude')

plt.tight_layout()
plt.show()