#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = dict()

for n in range(4):
    nota = float(input(f'{n+1}º Nota: '))
    notas[f'nota{n+1}'] = nota

notas['media'] = (notas['nota1'] + notas['nota2'] + notas['nota3'] + notas['nota4']) / 4

print('Notas:', end=' ')
for v in range(4):
    print(notas[f'nota{v+1}'], end='; ')
    
print(f"\nMedia: {notas['media']}")