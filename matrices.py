import random

def matriz1():
    matrices = []

    for fila in range(2):
        matrices.append([])
        for columna in range(2):
            matrices[fila].append("*")
    print(matrices)
matriz1()

def insertMatriz():
    filas = int(input("Digite el número de filas: "))
    columnas = int(input("Digite el número de columnas: "))

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)

    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = int(input("Elemento: %d %d : " % (f, c)))
    print(matriz)

insertMatriz()



def ejercicio1():
    matriz = []

    for fila in range(5):
        matriz.append([])
        for columna in range(5):
            matriz[fila].append(random.randint(0, 50))
            for n,i in fila:
                print(i)
    print(matriz)

ejercicio1()
