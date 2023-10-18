"""
22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
"""


def suma_acumulada (lista):
  total = 0
  for i in lista:
    total += i
  return total
print (suma_acumulada([1,3,5,4,9]))


def mas_comun (lista):
  from collections import Counter
  return Counter(lista).most_common (1)[0][0]
print (mas_comun([1,1,2,5,6,2,4,2]))


def tabla_multiplicar (n):
  return {i: i*n for i in range (1,11)}
print (tabla_multiplicar (5))


def cantidad_caracter (cadena):
  return {caracter: cadena.count (caracter) for caracter in cadena}
print (cantidad_caracter ('Casas'))


def no_comun (lista1,lista2):
  return (set(lista1) ^ set(lista2))
print (no_comun([1,2,3,4,5],[1,3,5,7]))


def no_duplicado (lista):
  return set (lista)
print (no_duplicado([1,2,2,3,4,1,5,2]))

def suma_pares_cuadrado (n):
  return sum (i**2 for i in range(2,n+1) if i % 2==0)
print (suma_pares_cuadrado(6))
