""" 
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
"""

def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
fibonacci(7)


def divisores(n):
  return [i for i in range(1, n + 1) if n % i == 0]
print (divisores (9))


def unico(lista):
  return list(set(lista))
print (unico(['yogur', 'leche', 'mantequilla', 'yogur', 'aceite', 'leche']))


def suma_digitos(n):
  return sum(int(digito) for digito in str(n))
print (suma_digitos(87))


def vocales_cadena (cadenas):
  return sum(1 for vocales in cadenas if vocales.lower() in 'aeiou')
print (vocales_cadena ('Me llamo Marina'))


def n_elemento_lista (lista,n):
  return lista [:n]
print (n_elemento_lista ([5,4,7,8,9,10,6],2))


def contar_may_min (cadena):
  mayusculas = sum (1 for letra in cadena if letra.isupper ())
  minusculas = sum (1 for letra in cadena if letra.islower ())
  return mayusculas,minusculas
print (contar_may_min('Mi nombre es Marina Alonso'))
