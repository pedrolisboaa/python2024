nome = 'Pedro Lisboa'
novo_nome = ''
tamanho = 0
while tamanho < len(nome):
    novo_nome += f'*{nome[tamanho]}'
    tamanho += 1
 
print(novo_nome)
