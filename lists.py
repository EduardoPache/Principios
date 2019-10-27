def users():
    listsName = []
    for i in range(0, 100):
        name = input("Ingresa tu nombre: \n")
        listsName.append(name)
        if(name == 0):
            print(sort(listsName))
            break
        else:
            name = input("Ingresa tu nombre: \n")