"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

quadrado = float(input('Digite o tamanho de um lado do quadrado e terá, '
                       'a área total e a dobrada em cm: '))
area = quadrado * quadrado
area_dobrada = area * 2

print(f'A área do quadrado é: {area}cm.\n'
      f'E a área do quadrado dobrada é: {area_dobrada}cm')
