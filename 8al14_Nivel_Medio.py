"""
8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
"""

def num_perfecto(n):
  return n == sum (i for i in range(1,n) if n % i == 0)
print (num_perfecto(8))


def a_binario(n):
  return bin(n).replace("0b", "")
print(a_binario(13))


def comun_ambas (lista1, lista2):
  return (set(lista1) & set(lista2))
print (comun_ambas (['Maca', 'Marina', 'lucas'], ['Marina', 'lorena', 'Migue']))


def palindromo (cadena):
    if cadena [::-1] == cadena:
     return ['Es un palindromo']
    else:
      return ['No es un palindromo']
print (palindromo ('salas'))


for i in range (1,51):
  if i % 3 == 0 and i % 5 == 0:
    print ('FizzBuzz')
  elif i % 3 == 0:
    print ('Fizz')
  elif i % 5 == 0:
    print ('Buzz')
  else: 
    print (i)


def orden_ascendente (lista):
  return sorted (lista)
print (orden_ascendente ([5,2,4,15,3,21,6,0]))


def palabra_larga (lista, n):
  return [i for i in lista if len(i)>n]
print (palabra_larga (['pan', 'arroz','leche', 'huevo', 'mantequilla', 'aceite'], 5))

