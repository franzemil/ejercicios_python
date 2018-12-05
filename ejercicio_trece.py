vocales = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
}

if __name__ == '__main__':
    cadena = input('Ingrese el texto: ')
    for letra in cadena:
        if letra in vocales:
            vocales[letra] += 1

    for k, n in vocales.items():
        print(k, end=' ')
    print('')

    for i in range(max(vocales.values())):
        for k, n in vocales.items():
            if n > i:
                print(k, end=' ')
            else:
                print(' ', end=' ')
        print('')
