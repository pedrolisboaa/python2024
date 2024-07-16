from random import randrange


senha = 1523659874536245
tentativa = 1
low = 0
high = 99999999999999999

while low <= high:
    sr = (low + high) // 2

    print(f'Senha: {senha} - achei {sr}')

    if senha == sr:
        print('São iguais')
        print(f'Realizei {tentativa} tentativas para descobrir.')
        break
    elif senha < sr:
        high = sr - 1
    else:
        low = sr + 1
    
    tentativa += 1