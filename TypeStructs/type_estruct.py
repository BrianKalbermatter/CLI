#Tipos de datos:
#Binario = 0b
#Hexadecimal = 0x
#Octal = 0o

#a = 0b10
#b = 0x10
#c = 0o10
#print(a, type(a))
#print(b, type(b))
#print(c, type(c))

#getsizeof() esta funcion devuelve tamano de una variable en memoria
#b = int(1.2)
#print(b, type(b))

#Booleanos
#print(bool([])) #Falso

#Los numeros complejos tienen Dos Partes
#Los numeros reales
#a = 2, "o", 7.2
#Los numeros imaginarios
#parte_real + parte_imaginaria * j
#b = 2 + 7j
#c = 2 - 7j

#Numeros Complejos en Python :
#d = 3 + 3j
#print(d)#(3 + 3j)
#print(type(d))#Class Complex
#print(d.real)
#print(d.imag)

#e = complex(1, 2)
#print(e)

#Suma de numeros complejos
a = 1 + 3j
b = 4 + 1j
print(a+b)
#Resta de numeros complejos
a = 1 + 3j
b = 4 + 1j
print(a-b)
#Multiplicacion de numeros complejos
a = 1 + 3j
b = 4 + 1j
print(a*b)
#Divisin de numeros complejos
a = 1 + 3j
b = 4 + 1j
print(a/b)
#Conjugado de numeros complejos
a = 1 + 1j
print(a.conjugate())

#Tambien se puede utilizar la libreria cmath que se utiliza para calcular "fases" en radianes
#Calcular polares que son los modulos o angulos
import cmath
print(cmath.phase(complex(5,0)))
print(cmath.polar(complex(5,5)))

s = "Esto es una cadena y puedo colocarle tambien \" esto tambien"
print(s)











