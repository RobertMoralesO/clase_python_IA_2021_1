#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:07:49 2021

@author: robertomorales
"""

# Ciclo  For en Python

for valor in range(10):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 100, 2):
    print(valor)
print("hola")

for i in range(1, 11):
    for j in range(1, 6):
        print(i, j)

# ciclo While

while True:
    print("hola")
    break

i = 2
while i <= 10:
    print(i)
    # i = i + 2
    i += 2


# HUA que de las n notas de un estudiante calcule el promedio
# académico final

notas = 0
numero_notas = int(input('Digite el número de notas del estudiante: '))
for i in range(1, numero_notas + 1):
    while True:
        nota = float(input(f'Digite la nota número {i}: '))
        if nota < 5 and nota > 0:
            break
    notas = notas + nota
prom = notas / numero_notas
prom = round(prom, 2)
print(f'El promedio académico final de las {numero_notas} notas es: {prom}')


# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'hola', 3.4]
c = [2, [True, False], ['hola', 'mundo'], [2.3, 3.4, 4.6, 7.8]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)


a[0] = 7
print(b[2])

a = [2, 3, 4]
a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina de la lista un elemento por su valor
a.pop()  # Elimina el último elemento del vector
a.pop(1)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos de la lista
b = a  # Asignación de b en el mismo espacio de memoria de a
id(a)  # Convierte en decimal la dirección en memoria de un objeto
b = a[:]  # Copia de los elementos de a
c = b[0:3]
c = b[:3]
c = b[2:]

# Tuplas
# Tipo de datos inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'hola', True, 4.5)
a = (1, ['hola', 'Mundo'], True, 4.5)
a = (1, ['hola', 'Mundo'], (True, False), 4.5)
b = a[:2]
4 in a


# Set
# Mutables y NO ordenados
a = {1, 2, 3, 4}
a = {7, 2, 1, 5, 9, 9}

# Diccionario
# Mutable pero no ordenado

a = {'nombre': 'Roberto', 'apellido': 'Morales'}
a = {1: 'Roberto', 2: 'Morales'}

a['nombre']
a['nombre'] = 'Carlos'

for valor in a:
    print(valor)

for valor in a.values():
    print(valor)

for key, valor in a.items():
    print(key, valor)

for valor in a.items():
    print(valor)


# Funciones


def nombre_funcion():
    pass


def saludar():
    print('Hola Mundo')


def saludar2(nombre):
    print(f'Hola {nombre}')


# Parámetros Opcionales
def saludar3(nombre='Mundo'):
    print(f'Hola {nombre}')


def saludar4(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')


# No se puede tener parámetros obligatorios despues de uno opcional
def saludar4(nombre="", apellido):
    print(f'Hola {nombre} {apellido}')


# Parámetros ilimitados
def saludar5(*nombres):
    for nombre in nombres:
        print(nombre)


saludar5('Roberto', 'Manuel', 'Sergio', 'Carlos')


def saludar6(**nombres):
    print(nombres)


saludar6(nombre='Roberto', nombre2='Carlos')


def saludar7(*nombres, **apellidos):
    print(nombres)
    print(apellidos)


saludar7('Roberto', 'Cesar', apellido1='Morales', Apellido2='Ortega')


def saludar8(nombre, apellido):
    print(f'Hola {nombre} {apellido}')


saludar8('Roberto', 'Morales')

saludar8(apellido='Morales', nombre='Roberto')


def suma(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    return suma


def suma2(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


def operaciones(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    resta = numero_uno - numero_dos
    mult = numero_uno * numero_dos
    div = numero_uno / numero_dos
    return suma, resta, mult, div


op = operaciones(3, 4)
suma, resta, mult, div = operaciones(3, 4)
_, _, _, div = operaciones(3, 4)


# HUA que dado los n elementos de un vector, calcule la sumatorio de estos
# elementos

numeros = []
numero_elementos = int(input('Digite el número de elementos del vector: '))
for i in range(1, numero_elementos + 1):
    numero = float(input(f'Digite el elemento número {i}: '))
    numeros.append(numero)
sumatoria = sum(numeros)
print(f'Vector final: {numeros}')
print(f'La sumatoria del vector es: {sumatoria}')
print(f'El elemento de menor valor del vector es: {min(numeros)}')
print(f'El elemento de mayor valor del vector es: {max(numeros)}')



# HUA que dado los n elementos de un vector, calcule la sumatorio de estos
# elementos

i = 1
numeros = []
while True:
    numero = float(input(f'Digite el elemento número {i} o digite 0 para salir: '))
    if numero == 0:
        break
    i += 1
    numeros.append(numero)
sumatoria = sum(numeros)
print(f'Vector final: {numeros}')
print(f'La sumatoria del vector es: {sumatoria}')
print(f'El elemento de menor valor del vector es: {min(numeros)}')
print(f'El elemento de mayor valor del vector es: {max(numeros)}')

































 