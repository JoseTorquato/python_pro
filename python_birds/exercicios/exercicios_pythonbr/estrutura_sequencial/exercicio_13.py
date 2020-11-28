"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.
Utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
sexo = input('Você é Homem (H) ou Mulher (M): ')
altura = float(input('Digite sua altura em metro (1.80) para descobrir seu peso ideal: '))

if sexo.upper() == 'H':
    peso_ideal_h = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal_h:.2f}KG.')
elif sexo.upper() == 'M':
    peso_ideal_m = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal_m:.2f}KG.')
else:
    print('Você não digitous seu sexo corretamente.')
