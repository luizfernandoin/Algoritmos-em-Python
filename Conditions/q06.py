#Escreva um programa que leia três números inteiros distintos e identifique o maior número lido.

'''
1º Forma: Utilizando de uma lista para armazenar os valores informados e o método sort() para ordenar os mesmo, o número maior encontra-se na ultima posição da lista.
'''

numeros = list()

for n in range(3):
    num = float(input(f'{n+1}º Número: '))
    numeros.append(num)

numeros.sort()
print(f'O maior número informado foi {numeros[2]}')

'''
2º Forma: Utilizando de uma lista para armazenar os valores informados e a variavel maior para armazenar o maior número, basta realizar verificações através de conditionals.
'''
'''
numeros = list()
maior = 0

for n in range(3):
    num = float(input(f'{n+1}º Número: '))
    numeros.append(num)

if numeros[0] >= numeros[1] and numeros[0] >= numeros[2]:
    maior = numeros[0]
elif numeros[1] >= numeros[0] and numeros[1] >= numeros[2]:
    maior = numeros[1]
elif numeros[2] >= numeros[0] and numeros[2] >= numeros[1]:
    maior = numeros[2]
    
print(f'O maior número informado foi {maior}')
'''