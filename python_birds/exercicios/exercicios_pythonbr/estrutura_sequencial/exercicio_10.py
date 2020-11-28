"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

"""

celsius = float(input('Quantos graus Celsius está: '))
fahrenheit = (celsius * (9/5)) + 32

print(f'Está fazendo {fahrenheit:.0f}º Fahrenheit')
