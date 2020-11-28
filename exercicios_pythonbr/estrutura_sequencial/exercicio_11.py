"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""

num_int_1 = int(input('Digite um número inteiro: '))
num_int_2 = int(input('Digite outro número inteiro: '))
num_real = float(input('Digite um número real: '))

primeiro_calc = (num_int_1 * 2) + (num_int_2 / 2)
segundo_calc = (num_int_1 * 3) + num_real
terceiro_calc = num_real ** 3

print(f'Produto do dobro do primeiro "{num_int_1}" + metade do segundo "{num_int_2}" é: {primeiro_calc}')
print(f'PA soma do triplo do primeiro número "{num_int_1}" + o número real "{num_real}" é: {segundo_calc}')
print(f'Número real "{num_real}" elevado ao cubo: {terceiro_calc}')
