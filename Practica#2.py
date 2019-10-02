

valorUno =  int(input("ingrese un numero entero:"))
valorDos = int(input("ingrese otro numero entero:"))
if valorUno != valorDos:
    if valorUno > valorDos:
        print("el ", valorUno ,"es mayor que ", valorDos,'es el menor' )
    else:
        print("El", valorDos ,'es mayor que el', valorUno,'es el menor')
else:
    print('coloque numeros diferentes')