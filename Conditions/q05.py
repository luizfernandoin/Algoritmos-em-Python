#Escreva um programa que leia os valores dos três lados de um triângulo e o classifique como equilátero, isósceles ou escaleno.

lados = dict()

for c in range(3):
    lado = float(input(f'{c+1}º Lado: '))
    lados[f'lado{c+1}'] = lado

if len(set(lados.values())) == 1:
    print('Triangulo equilatero!')
elif len(set(lados.values())) == 2:
    print('Triangulo isósceles!')
else:
    print('Triangulo escaleno!')