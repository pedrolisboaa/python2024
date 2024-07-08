nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

contem_espaco = nome.find(' ')
resposta_espaco = 'Seu nome contem espaço'
if contem_espaco == -1:
    resposta_espaco = 'Seu nome não contem espaço'



if not nome and not idade:
    print(f'Você deixou um dos campos em branco!')
else:

    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'{resposta_espaco}')
    print(f'Seu nome tem {len(nome.strip())} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'a última letra do seu nome é {nome[-1]}')