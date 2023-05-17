#Escreva um programa que leia as quatro médias de um aluno e verifique se o mesmo está aprovado por média, se fará prova final ou se está reprovado por média. Caso o aluno tenha que fazer a prova final, o programa deve informar quanto ele terá que tirar na prova. Você pode considerar que a média mínima para a aprovação por média é 7 e que a média mínima para fazer a prova final é 4. O cálculo da prova final é calculado através da fórmula abaixo.

medias = dict()

for m in range(4):
    media = float(input(f'{m+1}º Média: '))
    medias[f'media{m+1}'] = media


# Calcula a média final
soma_medias = 0
for media in medias.values():
    soma_medias += media
    
media_final = soma_medias / 4

# Verifica se o aluno está aprovado, fará prova final ou está reprovado
if media_final >= 7:
    print("O aluno está aprovado por média.")
elif media_final >= 4:
    print("O aluno fará prova final.")
    nota_necessaria = ((media_final * 6) - 50) / 4
    if nota_necessaria < 0:
        nota_necessaria = nota_necessaria * -1
    print(f"O aluno precisa tirar {nota_necessaria:.2f} na prova final para ser aprovado.")
else:
    print("O aluno está reprovado por média.")
