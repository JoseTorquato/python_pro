"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

horas_trabalhada = float(input('Quantas horas você trabalhou nesse mês: '))
valor_hora = float(input('Quantas ganha hora: '))

salario_mes = horas_trabalhada * valor_hora

print(f'Você irá receber R${salario_mes:.2f}.')
