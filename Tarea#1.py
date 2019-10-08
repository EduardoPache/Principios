#print("Bienvenidos a mis tareas del Curso de python \n")

task = [
    "Tarea #1",
    "Tarea #2",
    "Tarea #3",
    "Tarea #4",

]

#for i in task:
    #print(i ,"\n")


#tarea =  int(input("Ingresa el numero de la tarea que te gustaria ver? \n "))



def tarea1():
    print("Bienvenidos, Sistema de Sumatizacion entre un rango de dos numeros enteros")

    valor1 = int(input("Ingrese el primer numero del rango de suma: "))
    valor2 = int(input("Ahora el numero final del rango: "))

    if valor1 < valor2:
        for i in range(valor1+1,valor2):
            w = sum(range(valor1+1, valor2))
            print(i)
    else:
        print("ingrese el valor menor de primero!!!")


    print("La suma es", w)

def tarea2():
    print("Bienvenidos, Crea tu cuadrado con asteriscos ")

    altura = int(input("Ingrese la altura: "))
    ancho = int(input("Ingrese el ancho: "))


    for i in (altura, ancho):
        print("*")
     
def tarea5():
    nom = str(input("Bienvenidos \n Cual es tu nombre?"))
    sex = input("Eres hombre o Mujer? (M o H)")
    anno = int(input("Cuantos años tienes? "))
    


    if( sex == "H" or sex == "h"):
        if( anno < 30):
            print(nom,", tu monto a pagar es $3000")
        else:
            print(nom,", tu monto a pagar es $50000")
    else:
        if(anno < 21):
            print(nom, ", tu monto a pagar es $8000")
        else:
            print(nom, ", tu monto a pagar es $10000")


def tarea11():
    ndias =  int(input("Bienvenido \n Cuantos dias quieres ingresar? "))


    totalAnno = int(ndias/365)
    totalMeses = int(ndias/30)
    totalSem = int(ndias/7)

    print("Años: ", totalAnno, "Meses: ", totalMeses, "Semanas: ", totalSem, "Dias: ", ndias)

def menu():
    if(tarea == 1):
        tarea1()
    elif(tarea == 2):
        pass
 
tarea11()
