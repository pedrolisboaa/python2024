n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))

if n1 > n2:
    print(f'O número {n1} é maior que o {n2}.')
elif n1 < n2:
    print(f'O número {n2} é maior que o {n1}.')
else:
    print(f'Os números são iguais.')