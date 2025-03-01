import keyword

from LearnLogicBasicPy.funct import Unpacking
#Para colocar procesos por consola
import subprocess
import sys
class MiPrimeraClase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    # Método de la clase
    def functFirst ():
        colocarnumero = int(input("Coloque un número: "))
        if (colocarnumero < 1):
                if (colocarnumero < 1):
                    print(colocarnumero, "es menor que 1")
                else:
                    print(colocarnumero, "es igual a 1")
        elif (colocarnumero > 1):
            print(colocarnumero, "es mayor que 1")
        else:
            print(colocarnumero, "es igual a 1")


class MiSegundaClase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    # Método de la clase
    def functSecond ():
        #Algortmo de comienzo
        print("Bienvenido al algoritmo")#Cadena de texto
        print(keyword.kwlist)
        #instancias de variables
        num1 = 0
        num2 = 0
        num3 = 0

        #Asignación de valores
        #Necesito colocar un diccionario de valores para que pueda almacenar string de texto, como agenda de contactos y hacer funcionalidades de busqueda, insercion, actualizacion en CRUD.
        dict = {"nombre": "Juan", "edad": 22}
        print(dict)


        #Lista
        a = list("Hola Mundo")
        print(a)
        #Entrada de datos
        num1 = int(input("Escriba un número: "))
        num2 = int(input("Escriba un número: "))
        num3 = int(input("Escriba un numero: "))
        result = num1 ** num2 / num3 
        cadena = input("Escriba una cadena de texto: ")
        print(f"Mi cadena de texto es: {cadena}")
        print(result)
        print("Fin del algoritmo")

#CLase del Bucle while
class MiPrimerBucleWhile:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def blucleWhile(self):
        num1 = int(input("Escriba un número: "))
        while num1 <= 1000:
            print(num1)
            num1 += 1
        
        print("Fin del bucle while")







opciones = input("Comenzar Menu:")
#while opciones  != 5:
#    print("Menu de opciones")
#    print("1. Opción 1")
#    print("2. Opción 2")
#    print("3. Opción 3")
#    print("4. Opción 4")
#    print("5. Salir")
#    casos = int(input("Elija una opción: "))
#    match casos:
#        case 1:
#            print("Soy el caso 1."," Entraste en condiciones anidadas")
#            num1 = 30
#            num2 = 20
#            if (num2 > num1):# True
#                print("num1 es mayor que num2")
#                if(num1 == 10):#False
#                    print("num1 es igual a 10")  
#            elif(num1 == num2):#False
#                print("num1 es diferente de num2")
#                if(num1 == 20):#False
#                    print("num1 es 10")
#                elif(num2 == 20):#True
#                    print("num2 es 20")    
#                else:
#                    print("Ninguno de los dos es verdadero")
#            elif(num1 < num2):
#                print("num1 es menor que num2")
#            else:
#                print("Ninguna de las condiciones anteriores es verdadera")
#        case 2:
#            print("Soy el caso 2")
#        case 3:
#            print("Soy el caso 3")
#        case 4:
#            print("Soy el caso 4")
#        case 5:
#            print("Salir")
#            break
#        case _:
#            print("Opción no válida") 
#
class Calculadora:
#    def funct():
#        subprocess.run(["python", "opciones.py"])
#
#if __name__ == "__main__":
#    Experimentando.funct()


    def sumar(self, numero1, numero2):
        return numero1 + numero2
    

    def restar():
        print("Restar")
        
    def multiplicar():
        print("Multiplicar")
    def dividir():
        print("Dividir")
    def potencia():
        print("Potencia")
    def modulo():
        print("Módulo")
    
    numero1 = int(input("Escriba un número: "))
    numero2 = int(input("Escriba un número: "))

    
    #No esta funcionando porque da error en los dos numeros que dice que necesitan ser nombrados.
    #Unir todo para que se pueda correr todo correctamente paso a paso y no solo sea una calculadora sino que este todo conectado con todas las funciones y clases.

#LLamando a las clases y funciones
calc = Calculadora()
print(calc.sumar(10, 20))
print(calc.restar(10, 20))
print(calc.multiplicar(10, 20))
print(calc.dividir(10, 20))
print(calc.potencia(10, 20))
print(calc.modulo(10, 20))










print("Fin del programa")





