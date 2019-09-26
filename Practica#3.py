

valorUno =  int(input("ingrese valor #1:"))
valorDos = int(input("ingrese valor #2:"))
valorTres = int(input("ingrese valor #3:"))

if (valorUno != valorDos) and (valorUno != valorTres) and (valorDos != valorTres):
    if (valorUno > valorDos) and (valorUno > valorTres):
        if (valorDos > valorTres):
            print( valorUno, " mayor y", valorTres, 'es menor')
        else:
            print(valorUno, 'es mayor', valorDos ,'es menor')
    elif (valorDos > valorUno) and (valorDos > valorTres):
        if (valorUno > valorTres):
            print( valorDos, " mayor y", valorTres, 'es menor')
        else:
            print(valorDos, 'es mayor', valorUno ,'es menor')
    elif (valorTres > valorDos) and (valorTres > valorUno):
        if (valorDos > valorUno):
            print( valorTres, " mayor y", valorUno, 'es menor')
        else:
            print(valorTres, 'es mayor', valorDos ,'es menor')





