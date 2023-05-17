#Escreva um programa que leia um número inteiro entre 1 e 10 e imprima o número lido por extenso.

while True:
    num = int(input('Número [1-10]: '))
    if 0 < num < 11:
        break

if num == 1:
    print('Um')
elif num == 2:
    print('Dois')
elif num == 3:
    print('Três')
elif num == 4:
    print('Quatro')
elif num == 5:
    print('Cinco')
elif num == 6:
    print('Seis')
elif num == 7:
    print('Sete')
elif num == 8:
    print('Oito')
elif num == 9:
    print('Nove')
elif num == 10:
    print('Dez')