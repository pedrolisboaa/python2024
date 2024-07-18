nome = 'pedro'
lista = list(nome)
lista_de_numeros = list(range(20))

print(lista)
print(lista_de_numeros)

lista[0] = 'P'
print(lista)
lista.append(' ')
lista.append('H')
print(lista)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

c.extend(a)
print(c)