
#? Multiplicar dos numeros sin el simbolo

# num1 = input('digite el primer numero')
# num2 = input('Digite otra numero')
# total = 0

# for i in range(int(num2)):
#     total += int(num1)

# print(total)

#? imprimir nombre al reves

# nombre = input('Digite el nombre')

# for i in nombre[::-1]:
#     print(i, end='')

#? Mostrar numero menor de una lista

# import random
# lista = []

# for i in range(15):
#     lista.append(random.randint(-5,20))

# print(lista)

# menor = lista[0]

# for i in lista:
#     menor = i if i < menor else menor

# print('El numero menor de la lista es: {}'.format(menor))

#? Encontrar el volumen de una esfera

# import math
# def volumenEsfera(radio):
#     total = 4/3 * math.pi * radio ** 3
#     return total

# radio = input('Digite el radiod e la esfera: ')
# try:
#     radio = float(radio)
# except:
#     print('No es un numero')


# print('el radio de la esfera es:', volumenEsfera(radio))

#? Escribir una clase con un metodo que indique si un usuario es mayor de edad

# class Usuario:
#     def __init__(self, nombre, edad) -> None:
#         self.nombre = nombre
#         self.edad = edad

#     def mayorDeEdad(self):
#         if self.edad >= 18:
#             return self.nombre + 'Es mayor de edad'
#         else:
#             return self.nombre + 'Es menor de edad'

# try:
#     edad = int(input('Digite la edad: '))
# except:
#     print('Esto no es una edad')

# user = Usuario('Jersson', edad)
# print(user.mayorDeEdad())    

#? Escribir cuantas vocales tiene una palabra

# s = input('Digite una palabra: ')
# vocales = ['a','e','i','o','u']
# cont = 0

# for l in s:
#     if l.lower() in vocales:
#         cont += 1

# print(f'La palabra {s} tiene un total de {cont} vocales.')

#? Escribir una aplicacion que reciba numeros infinitos hasta que se escriba basta, luego imprimir la suma de los numero

# suma = 0

# while True:
#     new = input('digite un numero a sumar o si quiere parar, escriba "basta": ')

#     if new == "basta":
#         print(suma)
#         break

#     try:
#         suma += int(new)
#     except:
#         print("No digito un numero pero tampoco la palabra basta")

#? Escribir una funcion que reciba su nombre y apellido y los agregue en un archivo

# file = open('mi nombre.txt', 'w')
# nombre = input('Su nombre es: ')
# file.write(nombre + '\n')
# apellido = input('Su apellido es: ')
# file.write(apellido + '\n')
# file.close()
