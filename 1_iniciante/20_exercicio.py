frase = 'o python e uma linguagem de programação multiparadigma. python foi criado por guido van rossum.'


letra = frase[0]
quantidade_de_vezes = frase.count(letra)
contador = 0


while contador < len(frase):
    nova_letra = frase[contador]
    vezes_dois = frase.count(nova_letra)


    if vezes_dois > quantidade_de_vezes:
        if nova_letra == ' ':
            pass
        else:
            quantidade_de_vezes = vezes_dois
            letra = nova_letra
    
    contador += 1


print(f'A letra que aparece mais vezes é o {letra} ela aparece {quantidade_de_vezes}.')
 
