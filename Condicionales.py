""""" 
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
"""

a = -5
if a>0:
  print ('positivo')
else:
  print ('negativo')


a = 4
if a % 2 == 0:
  print ('par')
else:
  print ('impar')


a = 4
b = 0
c = -2
mayor = max (a, b, c)
print(mayor)
