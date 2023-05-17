#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for n in range(10):
    num = int(input(f'{n+1}º Número: '))
    numeros.append(num)

numeros.sort(reverse=True)
print('Números:', end=' ')
for valor in numeros:
    print(valor, end=' ')