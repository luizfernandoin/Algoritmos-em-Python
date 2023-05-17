#Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar

numero = int(input('Número: '))

if numero == 0:
    print(f'O número {numero} é neutro.')
else:
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar.')