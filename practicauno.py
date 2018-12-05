cadena = input('Ingrese su cadena: ')

if cadena == ''.join(list(reversed(cadena))):
    print("Palindromo")
else:
    print("No Palindromo")
