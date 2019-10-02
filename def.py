def estudiante():
    nombre = input("Cual es tu nombre: ")

    print('Mi nombre es ', nombre)



def calcular():
    valor1 = int(input("Digite un valor: "))
    valor2 = int(input("Digite otro valor: "))

    if (valor1 < valor2):
        print(valor2, 'es el valor mayor')
    else:
        print(valor1, 'es el valor mayor')


def numeroPositivo():
    valor = int(input('Ingrese un numero '))

    if (valor > 0):
        print("El valor es positivo")
    else:
        print('El valor es negativo')

def colores():
    valor = input("Ingrese A si quiere amarillo o R si quiere rojo: ")
    A = "amarillo"
    R = "rojo"

    if( valor == "A"):
        print(A)
    else:
        print(R)

def  respuesta():
    valor = input("Ingrese su respuesta? (Si o No?) ")

    if(valor == "Si"):
        number1 = int(input("Ingrese un numero: "))
        number2 = int(input("ingrese otro numero: "))

        if(number1 < number2):
            print(number1, number2)
        else:
            print(number2,number1)
    else:
        print("hasta la vista")

respuesta()
