"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota_1 = float(input('Digite a nota do 1º bimestre: '))
nota_2 = float(input('Digite a nota do 2º bimestre: '))
nota_3 = float(input('Digite a nota do 3º bimestre: '))
nota_4 = float(input('Digite a nota do 4º bimestre: '))


media_notas = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'A média das notas são: {media_notas}.')
