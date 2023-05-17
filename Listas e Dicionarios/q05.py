#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = dict()

for aluno in range(10):
    notas = list()
    print('=-='*10)
    print(f'{aluno+1}º Aluno')
    print('=-='*10)
    for n in range(4):
        nota = float(input(f'{n+1}º Nota: '))
        notas.append(nota)
    alunos[f'aluno{aluno+1}'] = notas

print(alunos)

aprovados = 0
for aluno in alunos.values():
    media = sum(aluno) / 4
    if media >= 7.0:
        aprovados += 1

print(f"{aprovados} alunos tiveram média maior ou igual a 7.0")