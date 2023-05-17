#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor ímpar. Imprima os três vetores.

numeros = []
pares = []
impares = []

for n in range(20):
    num = int(input(f'{n+1}º Número: '))
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)

print(f'Números: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')