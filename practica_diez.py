if __name__ == '__main__':
    cadena = input('Ingrese su cadena: ')

    size_cadena = len(cadena)
    if size_cadena % 2 == 0:
        raise ValueError('Solo cadenas impares')

    medio = int((size_cadena - 1) / 2)

    print(cadena)
    for i in range(medio):
        print(' ' * (i + 1), end='')
        print(cadena[i + 1: medio] + cadena[medio: size_cadena - i - 1])
