"""
15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
"""

# 15. ejercicio --> no lo entiendo bien, no se resolverlo.


def mayor_lista (lista):
  return max(lista)
print (mayor_lista ([4,8,5,7,12,6,52,14]))


def suma_digitos_al_cubo (n):
  return (sum (int(digito)**3 for digito in str (n)))
print (suma_digitos_al_cubo (12))

def segundo_mayor (lista):
  return sorted(set(lista), reverse=True)[1]
print (segundo_mayor ([1,4,6,8,2,8]))

def comun (lista1,lista2):
  if set(lista1) & set (lista2):
    return True
  else:
    return False
print (comun (['ana', 'rocio', 'laura'], ['rocio', 'elena', 'marina']))


def inverso (lista):
  return lista[::-1]
print (inverso ([1,2,3,4,5]))

def contar (cadena):
  numeros = sum(i.isdigit() for i in cadena)
  letras = sum(i.isalpha() for i in cadena)
  return numeros,letras

print (contar ('Marina nació en el 1994'))
  
