"""
29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
"""

def promedio (lista):
  return [sum (lista)/ len (lista)]
print (promedio ([1,2,3,4,5]))


def cadena_mas_larga (lista):
  return max (lista, key=len)
print (cadena_mas_larga (['azul','amarillo','rojo','verde','negro']))

def es_primo(num):
  if num < 2:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True
def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append (numero)
    numero += 1
  return primos
print(primeros_n_primos(3))


def cadena_inversa (cadena):
  return ' '.join (cadena.split() [::-1])
print (cadena_inversa (("Hola Marina")))

def ordenar_ultimo_elemento (tuplas):
  return sorted (tuplas, key=lambda x: x[-1])
print (ordenar_ultimo_elemento(((1,2),(4,3),(2,1))))


def contar_vocales (cadena):
  return sum (1 for vocales in cadena if vocales.lower() in 'aeiou')
print (contar_vocales (('Me llamo Marina')))


def es_primo (n):
  for i in range (1,n+1):
    if n % i == 0:
      return True
    else:
      return False
print (es_primo (17))
