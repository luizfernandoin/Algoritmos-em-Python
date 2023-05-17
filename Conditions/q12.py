#Escreva um programa que leia dois operandos inteiros e um operador (+, -, *, /) e aplique o operador lido aos dois operandos, na ordem em que os mesmos foram digitados.


num1 = int(input('1º Número: '))
num2 = int(input('2º Número: '))
operacao = str(input('Informe a operação (+, -, *, /): ')).strip()
print('=-='*10)

if operacao == '+':
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')

elif operacao == '-':
    sub = num1 - num2
    print(f'{num1} - {num2} = {sub}')
    
elif operacao == '*':
    multi = num1 * num2
    print(f'{num1} x {num2} = {multi}')
    
elif operacao == '/':
    divi = num1 / num2
    print(f'{num1} / {num2} = {divi}')

else:
    print('Operação Inválida!')
    
  

  