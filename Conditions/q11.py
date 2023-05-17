# Escreva um programa que leia o peso e a altura de uma pessoa e verifique se ela está dentro da faixa de peso adequada, ou se está abaixo ou acima do peso. Para resolver este programa, considere que o IMC ideal para uma pessoa deve estar entre 18 e 25.

peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / altura ** 2
  
print(f'IMC: {imc:.2f}')

if 16 <= imc <= 16.99:
    print('Baixo Peso Grau II!')
elif 17 <= imc <= 17.99:
    print('Baixo Peso Grau I!')
elif 18 <= imc <= 25:
    print('Peso ideal!')
elif 25 < imc <= 29.99:
    print('Sobrepeso!')
elif 30 <= imc <= 34.99:
    print('Obesidade Grau I!')
elif 35 <= imc <= 39.99:
    print('Obesidade Grau II!')
else:
    print('Seu IMC não corresponde a nenhuma das condições.')
