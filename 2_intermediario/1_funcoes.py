def ola_mundo():
    print('Olá, mundo! - 1')
    print('Olá, mundo! - 2')
    print('Olá, mundo! - 3')


def falar_nome(nome):
    print(f'Ola {nome.upper()}!')


for i in range(10):
    ola_mundo()

falar_nome('pedro')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)