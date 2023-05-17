#Escreva um programa que leia três números inteiros distintos e identifique o maior e o menor número lido.


numeros = list()

for n in range(3):
    num = float(input(f'{n+1}º Número: '))
    if num in numeros:
        while True:
            print(f'O número {num} já foi informado!')
            num = float(input(f'{n+1}º Número: '))
            if num not in numeros:
                numeros.append(num)
                break
    else:
        numeros.append(num)

numeros.sort()
print(f'''
      O maior número informado foi {numeros[2]}
      O menor número informado foi {numeros[0]}''')


'''
numeros = list()
maior = 0
menor = 0

for n in range(3):
    num = float(input(f'{n+1}º Número: '))
    if num in numeros:
        while True:
            print(f'O número {num} já foi informado!')
            num = float(input(f'{n+1}º Número: '))
            if num not in numeros:
                numeros.append(num)
                break
    else:
        numeros.append(num)


if numeros[0] >= numeros[1] and numeros[0] >= numeros[2]:
    maior = numeros[0]
    if numeros[1] > numeros[2]:
        menor = numeros[2]
    else:
        menor = numeros[1]
elif numeros[1] >= numeros[0] and numeros[1] >= numeros[2]:
    maior = numeros[1]
    if numeros[0] > numeros[2]:
        menor = numeros[2]
    else:
        menor = numeros[0]
elif numeros[2] >= numeros[0] and numeros[2] >= numeros[1]:
    maior = numeros[2]
    if numeros[0] > numeros[1]:
        menor = numeros[1]
    else:
        menor = numeros[0]
    
print(f'O maior número informado foi {maior}')
print(f'O menor número informado foi {menor}')
'''