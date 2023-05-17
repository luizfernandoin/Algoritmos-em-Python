#Foram anotados os nomes, as idades e as alturas de 15 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# criar vetores vazios para armazenar as informações
alunos = (
    {"nome": "João", "idade": 20, "altura": 1.75},
    {"nome": "Maria", "idade": 18, "altura": 1.60},
    {"nome": "Pedro", "idade": 21, "altura": 1.80},
    {"nome": "Ana", "idade": 19, "altura": 1.70},
    {"nome": "Lucas", "idade": 22, "altura": 1.85},
    {"nome": "Fernanda", "idade": 23, "altura": 1.68},
    {"nome": "Carlos", "idade": 20, "altura": 1.72},
    {"nome": "Juliana", "idade": 19, "altura": 1.65},
    {"nome": "Ricardo", "idade": 21, "altura": 1.78},
    {"nome": "Luiza", "idade": 22, "altura": 1.82},
    {"nome": "Mariana", "idade": 24, "altura": 1.70},
    {"nome": "Gustavo", "idade": 19, "altura": 1.75},
    {"nome": "Beatriz", "idade": 20, "altura": 1.60},
    {"nome": "Thiago", "idade": 21, "altura": 1.85},
    {"nome": "Gabriela", "idade": 22, "altura": 1.68}
)

# calcular a média de altura dos alunos com mais de 13 anos
soma_alturas = 0
num_alunos = 0
for aluno in alunos:
    if aluno['idade'] > 13:
        soma_alturas += aluno['altura']
        num_alunos += 1


if num_alunos > 0:
    media_alturas = soma_alturas / num_alunos
else:
    media_alturas = 0

# determinar quantos alunos com mais de 13 anos têm altura inferior à média
num_alunos_baixa_altura = 0
for aluno in alunos:
    if aluno['idade'] > 13:
        if aluno['altura'] < media_alturas:
            num_alunos_baixa_altura += 1
            

# exibir o resultado na tela
print(f'Média de Alturas: {media_alturas:.2f}')
print(f"{num_alunos_baixa_altura} alunos com mais de 13 anos têm altura inferior à média de altura dos alunos com mais de 13 anos.")
