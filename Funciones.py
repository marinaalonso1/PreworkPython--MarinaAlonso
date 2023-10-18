"""
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa
"""

a = 5
b = 7
def suma (a, b):
  return a+b
print (suma (a,b))



a = 3
def factorial (a):
  if a == 0:
    return 1
  else:
    return a * factorial (a-1)
print (factorial (a))



a=19
def primo(a):
  for i in range(2, a):
    if a % i == 0:
      return 'no es primo'
  return 'es primo'
print(primo(a))



def suma_num (lista_num):
  total = 0
  for numero in lista_num:
    total += numero
  return total

list_num = (1,2,3,4,5,6,7,8,9)
print (suma_num(list_num))



a = "Marina"
def reversa_cadena (a):
  return (a [::-1])

print (reversa_cadena (a))