
lado1 = int(input("primer lado: "))
lado2 = int(input("segundo lado: "))
lado3 = int(input("trecer lado: "))

if ( lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
    print("Es escaleno")
else:
    if (lado1 == lado2) and (lado2 == lado3 ) or (lado1 == lado3):
        print('es equilatero')
    else:
        print("es Isoceles")