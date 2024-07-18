cpf = '03716477127'
multiplicacao_1 = list(range(10, 1, -1))
multiplicacao_2 = list(range(11, 1, -1))

primeira_soma = []

# Primeira Verificação
soma_9_primeiros_digitos = list(cpf[0:9])

for index, numero in enumerate(soma_9_primeiros_digitos):
    numero = int(numero) * multiplicacao_1[index]
    primeira_soma.append(numero)

digito_verificador = 11 - (sum(primeira_soma) % 11)

if digito_verificador >= 10:
    digito_verificador = 0


# Segunra verificação
segunda_soma = []
soma_10_primeiros_digitos = list(cpf[0:10])

for index, numero in enumerate(soma_10_primeiros_digitos):
    numero = int(numero) * multiplicacao_2[index]
    segunda_soma.append(numero)

segundo_verificaor = 11 - (sum(segunda_soma) % 11)

if segundo_verificaor >= 10:
    segundo_verificaor = 0

condicao1 = str(digito_verificador) == cpf[9]
condicao2 = str(segundo_verificaor) == cpf[10]

if condicao1 and condicao2:
    print(f'O CPF {cpf} é verdadeiro.')
else:
    print(f'O CPF {cpf} não existe.')




