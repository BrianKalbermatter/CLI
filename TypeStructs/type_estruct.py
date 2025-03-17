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
print("\110\110")

#raw strings 
print(r"\110\110")

#Formateo de cadenas
#La funcion str() convierte en string lo que se pasa como parametro.
x = 5
s = "El numero es: " + str(x)
print(s)



#Otra forma es usando %. Por un lado tenemos: 
#%s
#% = indica que se quiere imprimir.
#s = tenemos a la variable a imprimir.

#Para imprimir una cadena se usaria %s o %f para un valor en coma flotante.
x = 10
d = "El numero es: %d " %x
print(d)

e = "Los numeros son %d y %d" % (5, 10)
print(e)

z = "Los numeros son {} y {}".format(5,10)
print(z)

g = "Los numeros de {a} y {b}".format(a=5, b=10)
print(g)

def funtion():
    return 20
h = f"Este es mi numero:\nNumero ={funtion()}\nVeinte"
print(h)



#Objetivo del dia = Mutabilidad del Libro de Python.

def funtionTwo():
    return 20
num = 20
result = funtionTwo() + num 
i = f"{num} + {funtionTwo()} = {result}"
print(i)
#Aprender mas cosas de Nvim. Leer la documentacion: Conocer como se trabaja en NeoVim

num2 = 20;num3 = 20
result2 = num2 + num3
print(result2)

#Se puede verificar en un string si una palabra esta dentro de una concatenacion asi:
print("mola" in "Python mola")
print("hola ?"in"como estas?")
#Para saber cuantos caracteres tiene una cadena de texto se utiliza la funcion len() asi:
print(len("Hola como estas? espero que estes bastante bien. Sabias que me gusta Python y quiero hacer una aplicacion. Aun la estoy pensando que hacer pero mientras estoy aprendiendo mas sobre el lenguaje."))
#Tambien puedo convertir los float y int en strings
print("Esto es de los Strings")
flotante_decimal = str(10.5)
tipo = type(flotante_decimal)
print(flotante_decimal)
print(tipo)

o = "abcdefg"
print(o[0])
print(o[4], o[6])
print(len(o))
print(o[0:6])
print(o[0:2])
print(o[0:])









