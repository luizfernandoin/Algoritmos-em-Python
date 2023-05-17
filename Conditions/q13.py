#Escreva um programa que leia um número inteiro entre 1 e 12 correspondente a um mês do ano e verifique o trimestre a que este mês pertence.

mes = int(input("Digite o mês (em número): "))

if 0 < mes <= 3:
    trimestre = 1
elif 3 < mes <= 6:
    trimestre = 2
elif 6 < mes <= 9:
    trimestre = 3
elif 9 < mes <= 12:
    trimestre = 4
else:
    trimestre = 0

if trimestre != 0:
    print(f"O mês referido está no {trimestre}º Trimestre!")
