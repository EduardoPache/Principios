def comparacionValor():
    n1 = int(input("ingrese un numero: "))
    n2 = int(input("ingrese otro numero: "))

    if(n1 > 20):
        print("el valor de las dos variables: ", n1,n2)




def escribeMedia(x,y):
    resultado = (x+y)/2 
    return resultado

a = 3
b = 5
media = escribeMedia(a,b)
#print("la media de", a," y ",b," es:", media)

def divisor():
    dividendo = 5
    divisor = 3
    try:
        cociente = dividendo/divisor
        print(cociente)
    except:
        print("no se permite la division por cero.")


nx = int(input("Ingrese un numero: "))
nz = int(input("Ingrese otro numero: "))



def prueba(valor):
    if( valor == True):
        n2 = "hola"
        print(n2)
    else:
        
        print(valor)


valor = (nx < 10) and (nz > 0)
prueba(valor)
