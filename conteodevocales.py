cadena = 'Hola mundo' # type: ignore
vocales = 'aeiouAEIOU'
contador = sum(1 for letra in cadena if letra in vocales)
print('Numero de vocales:', contador)
