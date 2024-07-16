while True:
    sair = input('Quer sair? [s]im: ')
    if sair.upper() == 'S':
        break
    
    numero_1 = int(input('Informe o primeiro número: '))
    numero_2 = int(input('Informe o segundo número: '))
    operacao = input('Inform qual o peracao deseja:\n[A]dição \n[S]ubtração \n[M]ultiplicação \n[D]ivisão\n').lower()

    if operacao == 'a':
        print(f'A soma de {numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operacao == 's':
        print(f'A subtração de {numero_1} - {numero_2} = {numero_1 - numero_2}')
    elif operacao == 'm':
        print(f'A multiplicação de {numero_1} X {numero_2} = {numero_1 * numero_2}')
    elif operacao == 'd':
        if numero_2 == 0:
            print(f'O número não pode ser dividido por zero.')
            continue

        print(f'A divisao de {numero_1} / {numero_2} = {numero_1 / numero_2}')
    else:
        print('Operador não indetificado')
