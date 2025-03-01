from math import sqrt




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











