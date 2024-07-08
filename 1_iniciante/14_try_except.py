numero = input('Informe um número que ou dobrar. ')

try:
    numero = float(numero)
    print(f'O dobro de {numero} é {numero * 2}')
except:
    print(f'Isso não é um número {numero}')