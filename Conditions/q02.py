#Escreva um programa que leia dois números inteiros M e N e verifique se N é múltiplo de M.

m = int(input('Número M: '))
n = int(input('Número N: '))

if n % m == 0:
    print(f'O número {n} é multiplo de {m}')

elif n % m != 0:
    print(f'O número {n} NÃO é multiplo de {m}')
