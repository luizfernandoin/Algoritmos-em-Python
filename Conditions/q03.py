#Escreva um programa que leia um número inteiro e verifique se ele é positivo, negativo ou neutro.

numero = int(input('Número: '))

if numero < 0:
    print(f'O número {numero} é negativo.')
elif numero == 0:
    print(f'O número {numero} é neutro.')
else:
    print(f'O número {numero} é positivo.')
    