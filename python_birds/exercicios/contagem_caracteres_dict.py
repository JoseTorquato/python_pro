def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    ex:
    >>> contar_caracteres('Lucas')
    {'L': 1, 'a': 1, 'c': 1, 's': 1, 'u': 1}
    >>> contar_caracteres('Banana')
    {'B': 1, 'a': 3, 'n': 2}
     :param s:
    """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    """Teste"""
    print(contar_caracteres('Lucas'))  # chamando a função com parametro
    print()
    print(contar_caracteres('Banana'))
