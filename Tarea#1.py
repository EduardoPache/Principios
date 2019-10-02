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