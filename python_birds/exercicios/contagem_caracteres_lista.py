def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    ex:
    >>> contar_caracteres('Lucas')
    L: 1
    a: 1
    c: 1
    s: 1
    u: 1
    >>> contar_caracteres('Banana')
    B: 1
    a: 3
    n: 2
    :param s:
    """

    caracteres_ordenados = sorted(s)

    caracteres_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_anterior:
            contagem += 1
        else:
            print(f'{caracteres_anterior}: {contagem}')
            caracteres_anterior = caracter
            contagem = 1

    print(f'{caracteres_anterior}: {contagem}')


if __name__ == '__main__':
    """Teste"""
    contar_caracteres('Lucas')  # chamando a função com parametro
    print()
    contar_caracteres('Banana')
