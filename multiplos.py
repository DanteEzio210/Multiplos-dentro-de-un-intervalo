#Este programa imprime todos los números enteros, desde el entero "a" hasta el entero "b", que sean multiplos de "a"
#--------------------------------------------------------------------------------------------------------------------
#Entrada#
#Un entero 'a' y un entero 'b' separados por un espacio
#--------------------------------------------------------------------------------------------------------------------
#Salida#
#Todos los numeros enteros desde el entero 'a' hasta el entero 'b', que sean multiplos de 'a'
#--------------------------------------------------------------------------------------------------------------------

#                                          Ejemplo
# | Entrada  |    Salida    |   Descripción                                                              |
# |  10 44   | 10 20 30 40  | Todos los números enteros desde el 10 hasta el 44, que son multiplos de 10 |


rango = input()

a, b = rango.split()

a = int(a)
b = int(b)

for n in range(1, b+1):
    if n % a == 0:
        print(n,end=' ')