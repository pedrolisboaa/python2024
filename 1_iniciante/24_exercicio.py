nomes = ['pedro', 'rosangela', 'olivia']

for indice, nome in enumerate(nomes):
    print(f'{indice} - {nome}')


nome1, *nome2 = nomes

print(nome1)
print(nome2)