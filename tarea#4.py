#Tarea 4

#1 )
# import random
#
# class matriz():
#     def __init__(self, columna, fila):
#         self.columna = columna
#         self.fila = fila
#
#         matri = []
#
#         for i in range(fila):
#             matri.append([])
#             for j in range(columna):
#                 matri[i].append(random.randint(1, 20))
#
#         print(matri)
#
#         l = []
#         global r
#         global cer
#         global cin
#
#         for r in matri:
#             if(r[0] == 5):
#                 l.append("x")
#             else:
#                 l.append("c")
#
#
#
#         cin = l.count("x")
#         cer = l.count("c")
#
#         if(cin > 0):
#             print(" \n Filas que inician con 5 son", cin)
#         else:
#             print(" \n Filas que inician con 5 son cero")
#
#
# fila = int(input("Digite el numero de filas: "))
# columna = int(input("Digite el número de columnas: "))
#
# z = matriz(fila, columna)

#   #2)



def nA():
    archivo = open("data.txt", "w")
    archivo.write(persons)
    archivo.close()


m = True
persons = []

while m:
    class NombreEdad:
        def __init__(self, nombre, anno):
            self.nombre = nombre
            self.anno = anno

            global r



            if(nombre == "X"):
                r = False
            else:
                persons.append([nombre," ,",anno])
                print(persons)
                nA()


            print(r)





    nombre = input("Cual es tu nombre? ")
    anno = input("Cuantos años tienes? ")

    z = NombreEdad(nombre, anno)
    m = r
