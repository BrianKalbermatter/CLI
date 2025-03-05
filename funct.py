from math import sqrt
import time
from collections.abc import Iterable 

###############
class EscojaUnNumero:
    menssage = "Bienvenido a escoja su Numero"
    def funct1(self, menssage):
        def funct2(menssage):
            print(menssage)
        funct2(menssage)
    

    def funct3(self):
        def funct4():
            num1 = int(input("Número: "))
            
            if (num1 % 4 == 0):
                raiz_cuadrada = sqrt(num1)
                print(f"La raíz cuadrada de {num1} {raiz_cuadrada}")
            
            elif (num1 % 3 == 0):
                print(f"La raiz cuadrada es un numero impar por lo tanto la raiz cuadrada es: {num1}")
            
            else:
                print("No se puede realizar la operación")
        funct4()
    
###############


class TypingDuck:
    menssage = ("Hola soy un TypingDuck")
    def llamar_hablar(self, menssage):
            menssage.hablar()
    class Perro:
        def hablar(self):
            print("Guau!")
    class Pato:
        def hablar(self):
            print("Cuac!")
    class Gato:
        def hablar(self):
            print("Miau!")

    #llamar_hablar(Perro())
    #llamar_hablar(Pato())
    #llamar_hablar(Gato())






#Utilizando el metodo len
class Foo():
    def __len__(self):
        return 42
class Bar():
    pass

#print(len(Foo()))

####################################################################
# Utilizando el metodo iter
class Unpacking:
    
    def lista(self):
        #Listas en unas pocas lineas
        a, b, c, d, e, f = [1, 2, 3, 4, 5, 6]
        return a, b, c, d, e, f
    
    def tupla(self):
        #Tuplas en unas pocas lineas
        a, b, c, d, e, f = (1, 2, 3, 4, 5, 6)
        print(a, b, c, d, e, f)

    def dictionary(self):
        #Diccionarios en unas pocas lineas
        a, b, c, d, e, f = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis':6}
        print(a, b, c, d, e, f)

    def iterable(self):
        #Iterables
        a, b, c, d, e, f = "123456"
        print(a, b, c, d, e, f)

    def values(self):
        #Values
        a, b, c, d, e, f = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis':6}.values()  
        print(a, b, c, d, e, f)

    def range(self):
        #Range
        a, b, c, d, e, f = range(6)
        print(a, b, c, d, e, f)

    def unpacking(self):
        #Operador de Unpacking *
        *a, b = [1, 2, 3, 4, 5, 6]
        print(a, b)

    def unpacking_Dos(self):
        #extend()
        a = [1, 2]
        b = [3, 4]
        c = [*a, *b]
        print(c)    

    def dictionary_Unpacking(self):
        #Diccionarios usando **
        a = {'uno': 1, 'dos': 2}
        b = {'tres': 3, 'cuatro': 4}
        c = {**a, **b}
        print(c)


    def unpacking_Warning(self):
        #Si hay keys duplicados puede sobreescribirse con el que estaba primero o sea que tomara al ultimo que este en la lista
        a = {'uno': 1, 'dos': 2}
        b = {'uno': 0, 'dos': 0}
        c = {**a, **b}
        print(c)


    def bucle_For_Unpacking(self):
        #bucle for utilizando Unpacking
        for primero, *resto in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
            print("Primero:", primero)
            print("Resto:", resto)

###################################################

    def unpacking_For_Swapping(self):
        #Unpackin para Swapping
        a, b = (1, 2)
        print(a, b)

        a, b = b, a
        print(a, b)

    def operadores_Logicos(self):
        #Operadores Logicos
        a = True
        b = False

        print(a and b)
        print(a or b)
        print(not a)
        nor_result = not (a or b)
        print(nor_result)

    def operator_Tenario(self):
        #Operador Tenario
        x = 10
        print("Es 10" if x == 10 else "No es 10")#Tenary Operator

    def operator_Tenario_Dos(self):
        a = 11
        b = 12
        c = a/b if b !=0 else 0
        print(c)

    def numero_Par_Impar(self):
        #Verifica si un numero es par o impar
        x = 6
        if x % 2 == 0:
            print("Es par")
        else:
            print("Es impar")

    def condicion_De_Decremento(self):
        #Decrementa x en 1 unidad  si es mayor a 0
        x=5
        x -= 1 if x > 0 else x
        print(x)

#Bucles con For
#for <variable> in <iterable>:
#    <bloque de código>
class BucleFor:

    #Bucle For
    def bucle_For(self):
        for i in range(10):
            print(i)

    def bucle_For_Dos (self):
        for i in "Python":
            print(i)

    #Iterables
    def funct_Iterable(self):
        list = [1, 2, 3, 4, 5]
        cadena = "Python"
        numero = 12
        print(isinstance(list))#True
        print(isinstance(cadena))#True
        #print(isinstance(numero)#False

#Iteradores
#Un iterador es un objeto que permite recorrer un contenedor, pero no se puede acceder a los elementos directamente
    def funct_Iterador(self):
        list = [1, 2, 3, 4, 5]
        #Esta lista ocupa un espacio en memoria
        iterador = iter(list)
        print(iterador)
        print(type(iterador))

# str_iterator / para cadenas 
# list_iterator / para sets
# tuple_iterator / para tuplas
# set_iterator / para sets
# dict_keyiterator / para diccionario

class Iterador:
    def funct_Iterador_List(self):
        lista = [2, 3]
        it = iter(lista)
        print(next(it))
        print(next(it))
        #print(next(it)) esto daria un error porque no hay 3 numeros en la lista. Solamente 2.

    def funct_Iterador_MultiplesListas(self):
        lista1 = [2,3,4]
        it1 = iter(lista1)
        it2 = iter(lista1)
        print(next(it1))
        print(next(it1))
        print(next(it1))
        print(next(it2))

    def for_Anidados(self):
        lista3 = [[56, 34, 1], 
                [12, 4, 5], 
                [9, 4, 3]]
        for i in lista3:
            print(i)
        
        for i in lista3:
            for j in i:
                print(j)
    
    #Iterando cadenas de [::-1] desde el ultimo al primer elemento
    def bucle_For_Regresive_One(self):
        texto = "Python1"
        for var in texto[::-1]:
            print(var)
    #Iterando cadenas de [::-2] pero ahora sacando letras
    def bucle_For_Recort_Two(self):
        texto = "Python2"
        for i in texto[::-2]:
            print(i)

    #Comprehensions lists
    #print(sum(i for i in range(10)))
    def usingRange(self):
        for i in range(10):
            print(i) 
    
    #range() - Funcion
    print(list(range(5, 20 ,2)))

    #Mezclandolo con el range
    def mixing_Without_Range(self):
        for i in range(5, 20 ,2):
            print(i)
        #Secuencia inversa
        for j in range(5, 0, -1):
            print(j)
    
class Mientras:
    def iteracion_While(self):
        a = 10
        while a > 0:
            a -= 1
            print(a)
    
    def iteracion_While_One(self):
        b = 10
        while b > 0: b -= 1; print(b)
    
    def iteracion_While_Two(self):
        x = ["Uno", "Dos", "Tres"]
        while x:
            x.pop(0)
            print(x)

    def iterator_Else_While(self):
        x = 5
        while x > 0:
            x -= 1
            print(x)
            #break (Si hay un break aca el else no se cumple)
        else:
            print("El bucle a finalizado")
    
    def iterador_Else_While_Three(self):
        i, j, k = 0, 0, 0
        while i < 3:
            while j < 3:
                while k < 3:
                    print(i,j,k)
                    k += 1
                    j += 1
                k = 0
            i += 1
            j = 0
    
    def graphic_Tree_Chrisma(self):
        z = 7
        x = 1
        while z > 0:
            print(' ' * z + 'x' * x + ' ' * z)
            x+=2
            z-=1
    
    def text_Tree_List(self):
        text = "Python"
        i = 0
        while i < len(text):
            print(text[:i + 1])
            i += 1
    
    def fibonacci(self):
        a, b = 0, 1
        while b < 25:
            print(b)
            a, b = b, a + b

class SwitchInPython:
    #Emulando Switch
    #Lookup Tables
    def switchPython(self, condicion):
        #condicion = int(input("Coloque su condicion:\n->"))
        if condicion == 1:
            print("Haz a")
        elif condicion == 2:
            print("Haz b")
        elif condicion == 3:
            print("Haz c")
        else:
            print("Haz d")
    
    def switchPythonCalculator1(self):
        def calculator(self, operator, a, b):
            if operator == 'sumar':
                return a + b
            elif operator == 'restar':
                return a - b
            elif operator == 'multiplicar':
                return a * b
            else:
                operator == 'dividir'
                return a / b
        print(calculator)

    #Este esta almacenado en un diccionario
    def switchPythonCalculator2(self):
        def calculator(self, operator, a, b):
            return{
                'sumar' : lambda: a + b,
                'restar ' : lambda: a - b,
                'multiplicar' : lambda: a * b,
                'dividir' : lambda: a / b
            }.get(operator, lambda: None)
        print(calculator)
    
    class LearnLambda:
    #Se puede evitar escribir def con lambda. 
    #Se usa con varias funciones. 
        doblar = lambda x: x * 2
        print(doblar(4))
        #Lo que hace en esa funcion es multiplicar el numero de doblar * 2 = 8 y lo que se devuelve aca es la funcion lambda














##################################################################













class Switch1:
    tabla_switch = {
        "0" : "000",
        "1" : "001",
        }
    def usa_switch(self, decimal, tabla_switch):
        return tabla_switch.get(decimal, "NA")
    
    def usa_if(decimal):
        if decimal == '0':
            return "000"
        elif decimal == '1':
            return "001"
        elif decimal == '2':
            return "010"
        elif decimal == '3':
            return "011"
        elif decimal == '4':
            return "100"
        elif decimal == '5':
            return "101"
        elif decimal == '6':
            return "110"
        elif decimal == '7':
            return "111"
        else:
            return "NA"
    
    #A continuacion mediremos el "tiempo de ejecucion" de ambas para saber cual es mas rapida. Vamos a crear primero un "decorador" que nos permita medir el tiempo que una funcion tarda en ejecutarse.
    def mide_tiempo(function):
        def funtion_medida(*args, **kwargs):
            inicio = time.time()
            c = function(*args, **kwargs)
            print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}")
            return c
        return funtion_medida
    
    #Decoradores
    @mide_tiempo
    
    #Funcion para que se repita 1000000000 veces
    def repite_funtion(function, entrada):
        return [function(entrada) for i in range(10000000)]
    
    #No solamente pueden ser llamadas como print o como tal la funcion tambien puedo llamarla con for asi:
    for i in range(8):
        repite_funtion(usa_if, str(i))

    for i in range(8):
        repite_funtion(usa_switch, str(i))









###################################################################








#Match de casos
class ClassMatch:
    def funct_Match():
        hora = int(input("La hora que es: es "))
        match hora:
            case 8: 
                for i in range(3):
                    return i
            case 14:
                print("Desayunar")
            case 21:
                print("Almorzar")
            case 34:
                print("Cenar")
            case _:
                print("No Toca Comer")

#Uso del Break
class ClassBreak:
    x = 5
    while x > 0:
        x -= 1
        if x == 3:
            break
        print(x)

################################################

#Uso del Continue
class ClassContinue:
    x = 5
    while x > 0:
        x -= 1 
        if x == 3:
            continue
        print(x)


#Recorrer i-th de elementos
#i-esimo - Utilizando el len()
class IEsimo():
    lista_frutas = ["limones", "manzanas", "naranjas", "kiwis"]
    for i in range(len(lista_frutas)):
        print(f"El {i}-esimo{lista_frutas[i]}")
    tupla_frutas = ("limones", "manzanas", "naranjas", "kiwis")

#Uso de la funcion zip()
class ClassZip:
    def bucleForUnaLista():
        a = [1, 2]
        b = ["Uno", "Dos"]
        c = zip(a, b)
        print(list(c))

    def bucleForIterandoDosListas():
        a = [1, 2]
        b = ["Uno", "Dos"]
        c = zip(a, b)

        for numero, texto in zip(a, b):
            print("Numero", numero, "Letra", texto)
    
    def bucleForZipCon_N_Argumentos():
        numeros = [1, 2]
        espanol = ["Uno", "Dos"]
        ingles = ["One", "Two"]
        frances = ["Un", "Deux"]
        c = zip(numeros, espanol, ingles, frances)
        for n, e, i, f in zip(numeros, espanol, ingles, frances):
            print(n, e,i,f)

    def bucleForZip_Diferentes_Longitudes():
        numeros = [1, 2, 3, 4, 5]
        espanol = ["Uno", "Dos"]

        for n, e in zip(numeros, espanol):
            print(n, e)
    
    def bucleForZip_ConUnArgumento():
        numero = [1, 2, 3, 4, 5]
        zz = zip(numero)
        print(list(zz))

    #Resultado en Tuplas


    def bucleForZip_WithDictionaryOne():
        esp = {1 : "Uno", 2 : "Dos", 3 : "Tres"}
        ing = {1 : "One", 2 : "Two", 3 : "Three"}
        for e, i in zip(esp, ing):
            print(e, i)
    
    def bucleForZip_WithDictionaryTwo():
        esp = {1 : "Uno", 2 : "Dos", 3 : "Tres"}
        eng = {1 : "One", 2 : "Two", 3 : "Three"}
        #Con el items() podemos acceder al key y al value de un diccionario
        for (k1, v1) , (k2, v2) in zip(esp.items(), eng.items()):
            print(k1, v1, v2)   
    
    #Deshacer un zip() en una sola linea de codigo
    def listaABCDeshaciendoUnZip():
        a = [1, 2, 3]
        b = ["One","Two","Three"]
        c = zip(a, b)
        print(list(c))

    #Se puede obtener A y B desde C asi:
    def listaABCDeshaciendoUnZip_Dos():
        c = [(1, 'One') ,(2, 'Two') ,(3, 'Three')]
        a,b =zip(*c)
        print(a)
        print(b)
    #Notese el uso de *c unpacking en Python














#Para la proxima que quiera acceder a los indices de una coleccion, pensar que enumerete puede resolver mi problema mas clara

def enumerateInPython(self):
    listaUno = ["A", "B", "C"]
    for i in listaUno:
        print(i)

    #Este for se utiliza por si no solo queremos el elemento i-esimo de la coleccion, sino que ademas queremos el indice 
    listaDos = ["A", "B", "C"]
    self.indice = 0
    for a in listaDos:
        print(self.indice ,a)
        self.indice += 1
    
    #El verdadero enumerete 
    listaTres = ["A", "B", "C"]
    for indice, b in enumerate(listaTres):
        print(indice, b)

    listaCuatro = ["A", "B", "C"]
    en =list(enumerate(listaCuatro))
    print(en)
    
############################################
    
#List Comprehensions me permite crear listas de elementos en una sola linea de codigo.
class TheListComprehensions:
    
    def listComprehensionsOne():
        cuadrados = [i ** 2 for i in range(5)]
        print(cuadrados)
    
    def listComprehensionsTwo():
        cuadrados = []
        for i in range(5):
            cuadrados.append(i**2)
        print(i)
    
    #lista = [expresion for element in iterable]
    def listExpresionForElementInIterable():
        unos = [1 for i in range(5)]
        print(unos)

#    def eleva_Al_Dos(self ,i):
#        return i**2   
#    cuadrado = [eleva_Al_Dos(i); for i in range(5)]
    
    #Todos los numeros van a ser dividos por diez iterando con for en una lista
#    def listaDeNumeros(self, i):
#        lista = [42, 312,2,3,53,45]    
#        nuevaLista = [i/10; for i in lista]

    #Anadiendo Condicionales             
    #Control+J para abrir terminal
    #Expresion Generica
    #lista = [expresion for elemento in iterable if condicion]

    def condicionIfConvinadoConFor(self):
        frase = "El perro no tiene rabo y esta roto del ruleman las dos ratas que tienen rotas las parras del parro"
        erres = [i for i in frase if i== "r"]
        print(erres)

        #Se ejecuta una u la otra
        print(len(erres))
    print(condicionIfConvinadoConFor) 

    def devolviendoUnSet():
        frase = "El perro no tiene rabo y esta roto del ruleman las dos ratas que tienen rotas las parras del parro"
        #Aca en un set lo unico que cambia es {}
        my_set = {i for i in frase if i == 'r'}
        print(my_set)

        print(len(my_set))
        
    #Para un diccionario tengo que crear una variable para que se puedan llamar con el for por ejemplo:
    def dictionaryComprehension():
        lista1 = {'nombre', 'edad', 'region'}
        
        lista2 = {'Pelayo', 30, 'Australia'}

        mi_dict = {i:j for i,j in zip(lista1, lista2)}
        print(mi_dict)
    #Funciones filter y map




#Mal Uso de los Bucles para solucionar un problema con while o un for de la siguiente manera:
class bucleWhileProblema:
    def funcionBucleWhileProblema():
        lista = [5,4,3,2,1]
        i=0
        while i < len(lista):
            elementos = lista[i]
            print(elementos)
            i += 1

class bucleForProblema:
    def funcionBucleForProblema():
        lista = [5,4,3,2,1]
        i = 0
        for i in range(len(lista)):
            elementos = lista[i]
            print(elementos)
            
#La forma mas corta y facil de hacer un recorrido de manera que te muestre todos los numeros es:
class bucleCorrectoProblema:
    def funcionAlProblemaCorrecto():
        lista = [5,4,3,2,1]
        for i in lista:
            print(i)

#Iterables
#Una clase iterable es una clase que puede ser iterada a la derecha de un for asi:
#for elemento in [clase_iterable]:
#Iterable significa que es capaz de iterar un objeto a la vez, osea uno debajo del otro

libro = ['Pagina 1','Pagina 2','Pagina 3','Pagina 4']
marcapagina = iter(libro)
print(next(marcapagina))
print(next(marcapagina))
print(next(marcapagina))
print(next(marcapagina))
#StopIterection

class MiClase:
    def __init__(self, items):
        self.lista = items
    def __iter__(self):
        return iter(self.lista)

miObjeto = MiClase([5, 4, 3])
for items in miObjeto:
    print(items) 
#Esto dara error si no colocamos el __iter__(): 



