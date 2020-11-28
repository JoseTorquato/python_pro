"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peixe_trazido = int(input('Quantos KG de peixe você pescou hoje: '))

peso_excedente = peixe_trazido - 50
multa = peso_excedente * 4.00

if peixe_trazido<= 50:
    print(f'Você pescou "{peixe_trazido:.2f}KG" e não excedeu o limite.')
elif peixe_trazido > 50:
    print(f'Você pescou "{peixe_trazido:.2f}KG" e execedeu o peso em "{peso_excedente:.2f}KG".\n'
          f'E pagará uma multa de R${multa:.2f}.')
else:
    print('Algo de errado não está certo.')
