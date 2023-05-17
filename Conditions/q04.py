#Escreva um programa que leia a idade de uma pessoa e verifique se ela é criança (0-12 anos), adolescente (13-17 anos), adulta (18-59) ou idosa (acima de 60 anos).

while True:
    idade = int(input('Informe sua idade: '))

    if idade < 0:
        print('Informe uma idade válida!')
    else:
        if 0 <= idade <= 12:
            print('Você é criança!')
        elif 13 <= idade <= 17:
            print('Você é adolescente!')
        elif 18 <= idade <= 59:
            print('Você é adulto(a)!')
        else:
            print('Você é idoso(a)!')
        break