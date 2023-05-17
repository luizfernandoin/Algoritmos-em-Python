#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for n in range(5):
    num = int(input(f'{n+1}º Número: '))
    numeros.append(num)

print('Números:', end=' ')
for valor in numeros:
    print(valor, end=' ')