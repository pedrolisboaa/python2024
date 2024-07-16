contador = 1

while True:
    print(f'Contando {contador}')
    contador += 1
    if contador == 11:
        break


while True:
    nome = input('Informe seu nome: ')

    if nome == 'sair':
        break

    print(f'Olá {nome}!')

   
print('Acabou')


condicao = True
flag = 0
while condicao:
    flag += 1

    if flag % 2 != 0:
        continue
    else:
        print(f'{flag}')

    if flag == 101 or flag == 100:
        break
