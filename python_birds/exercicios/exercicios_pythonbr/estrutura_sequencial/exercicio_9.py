"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahrenheit = float(input('Quantos graus Fahrenheit está: '))
celsius = 5 * ((fahrenheit-32) / 9)

print(f'Está fazendo {celsius:.2f}º Celsius.')
