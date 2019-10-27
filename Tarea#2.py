# Numero 1

def ordenado():
    list = []
    list2 = []
    
    for i in range(5):
        num = int(input("ingresa un numero: "))
        list.append(num)
        list2.append(num)


    list2.sort()

    if(list == list2):
        return True
    else:
        return False


ordenado()

# Numero 2 
def primos():
    nu = int(input("Ingresa un numero: "))

    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    list.append(nu)

primos()

# Numero 3

def enteros():
    list3 = []

    for i in range(2):
        number = input("Ingrese un numero: ")
        list3.append(number)

    for item in list3:
        if (type(item) == int()):
            return True
        else:
            return False

enteros()



