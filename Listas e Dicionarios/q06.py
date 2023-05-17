#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.


'''1º Caso: Você pode utilizar a estrategia do exemplo anterior, armazenando um vetor para cada pessoa dentro de um dicionario {'pessoa1':[]}'''

pessoas = dict()
idades = []
alturas = []

for pessoa in range(5):
    informacoes = []
    
    print('=-='*10)
    print(f'{pessoa+1}º Pessoa')
    print('=-='*10)
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    informacoes.append(idade)
    informacoes.append(altura)
    idades.append(idade)
    alturas.append(altura)
    
    pessoas[f'pessoa{pessoa+1}'] = informacoes


'''2º Caso: Você pode criar um vetor para cada pessoa, o que não seria uma boa prática na programação. Imagina se fossem 200 pessoas?!'''