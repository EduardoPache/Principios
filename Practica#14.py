def usuarioTel():
    persons = {}
    
    for i in range(0, 1):
        name = input("nombre: ")
        tel = int(input("Telefono: "))
        if (name not in persons):
            persons[name] = tel
    print(persons)


def options():
    print("Cual opcion quieres realizar? ? \n 1---> Contar la cantidad de Mayusculas y minusculas o \n 2---> Contar cuantos caracteres especiales tiene el texto")
    x = int(input("Ingrese el numero: "))
    txt = str(input("ingrese el texto: \n "))
    
    def contarMayMin():    
        indice = 0
        minus = 0
        mayus = 0

        while indice < len(txt):
            letra = txt[indice]
            if letra.isupper() == True:
                mayus += 1
            else:
                minus += 1
            indice +=1
        print("Total de mayusculas: ", mayus)
        print("Total de minusculas: ", minus)

    def contarCaracter():
        indice = 0
        caracteres = 0
        especiales = "{!#$%&/()=?¡+-.;+´}[]{*"
        while indice < len(txt):
            caracter = txt[indice]
            if caracter.isascii() == True:
                caracteres += 1
            else:
                caracteres += 1
            indice += 1
        print("Total de caracteres: ", caracteres)
    

    if(x == 1):
        contarMayMin()
    elif (x == 2):
        contarCaracter()

options()


