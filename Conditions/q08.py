#Escreva um programa que leia três números distintos e identifique o número que não é nem o menor e nem o maior número.

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
print(f'O número intermediario é {numeros[1]}')



'''
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

if (numeros[0] > numeros[1] and numeros[0] < numeros[2]) or (numeros[0] > numeros[2] and numeros[0] < numeros[1]):
    intermediario = numeros[0]
    print(f"Número Intermediario: {numeros[0]}")
elif (numeros[1] > numeros[0] and numeros[1] < numeros[2]) or (numeros[1] > numeros[2] and numeros[1] < numeros[0]):
    intermediario = numeros[1]
    print(f"Número Intermediario: {numeros[1]}")
elif (numeros[2] > numeros[0] and numeros[2] < numeros[1]) or (numeros[2] > numeros[1] and numeros[2] < numeros[0]):
    intermediario = numeros[2]
    print(f"Número Intermediario: {numeros[2]}")
'''