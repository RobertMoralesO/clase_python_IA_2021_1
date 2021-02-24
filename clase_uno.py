print('Hello world')

# Variables
a = 3
print(type(a))
a = "hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# Operaciones

# suma
a = 5
b = 2
c = a + b
print(c)

# resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicación
a = 5
b = 2
c = a * b
print(c)

# División

a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# Potencia

a = 5
b = 2
c = a ** b
print(c)

# Raiz cuadrada
a = 16
b = a ** (1/2)
print(b)

# import math
# raiz = math.sqrt(16)
# print(raiz)

# Tipos de datos

# String str

a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Roberto"'
print(a)
print(b)
print(c)

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero
a = '3'
y = int(a)
print(y)
print(type(y))

# Convertir de x a decimal
a = 3
y = float(a)
print(y)
print(type(y))

# Convertir de x a String
a = 3
y = str(a)
print(y)
print(type(y))

# Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b
print(c)

a = 'hola'
b = a * 5
print(b)

# Capturar por pantalla

nombre = input('Digite su nombre: ')
print('Hola', nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)

# HUA que sume dos numeros e imprima su resultado
numero_uno = float(input('Digite el número uno: '))
numero_dos = float(input('Digite el número dos: '))
suma = numero_uno + numero_dos
# print(suma)
# print('La suma es:', suma)
print(f'La suma es: {suma}')

# HUA  que lea un número y lo eleve al cuadrado
base = int(input('Digite la base a elevar: '))
potencia = base ** 2
print(f'El resultado de elevar {base} al cuadrado es: {potencia}')

# HUA que tome el valor de un producto, le aplique el 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado


vproducto = float(input('Digite el valor del producto: $'))
descuento = vproducto * 0.2
vfinal = vproducto - descuento
print(f'El valor inicial del producto es: ${vproducto:,}')
print(f'El valor des descuento es: ${descuento:,}')
print(f'El valor ahorrado es: ${descuento:,}')


# Condicionales

# Tabla de verdad

# Tabla del and
# v and v = v
# v and f = f
# f and f = f
# f and v = f

# Tabla de verdad de or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

# Tabla del and
print(True and True)
print(True and False)
print(False and False)
print(False and True)

# Tabla del or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negación

print(not True)
print(not False)

# Jerarquía de operaciones
# 1. Paréntesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquía para operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad

# Mas de dos condiciones al mismo tiempo
print(True and False and True or False or True or True)
print(True and (False and True) or False or (True or True))

# Estructura if

if (x > 0):
    print('1')
else:
    print('2')
print('3')

# HUA que dada la edad de una persona indique si es mayor
# o menor de edad
edad = int(input('Digite la edad de la persona: '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# HUA que indique si un estudiante aprobó o reprobó una
# asignatura teniendo en cuenta que aprueba con mínimo
# una calificación de 3.0 hasta 5.0

nota = float(input('Digite el nota de la asignatura: '))
if nota >= 3:
    print(f'Aprobó la asignatura con una nota de {nota}.')
else:
    print(f'Reprobó la asignatura con una nota de {nota}.')

# HUA que indique si un estudiante aprobó o reprobó una
# asignatura teniendo en cuenta que aprueba con mínimo
# una calificación de 3.0, validando que sea una nota válida

nota = float(input('Digite el nota de la asignatura: '))
if nota < 0 or nota > 5:
    print(f'No es una nota válida')
elif nota >= 3:
    print(f'Aprobó la asignatura con una nota de {nota}.')
else:
    print(f'Reprobó la asignatura con una nota de {nota}.')

# HUA que dado un número n diga si es negativo, positivo o
# cero.

n = int(input('Digite el valor de n :'))
if n > 0:
    print(f'{n} es positivo')
elif n < 0:
    print(f'{n} es negativo')
else:
    print(f'{n} es cero')









