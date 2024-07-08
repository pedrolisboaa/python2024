"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
numero = input('Digite um número: ')

if numero.isnumeric():
    if int(numero) % 2 == 0:
        print(f'Seu número é Par.')
    else:
        print(f'Seu número é ímpar')
else:
    print('Isso não é um número inteiro.')

"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print(f'Seu nome é pequeno.')
elif len(nome) <= 6:
    print(f'Seu nome é normal.')
else:
    print(f'Você tem um nome grande.')