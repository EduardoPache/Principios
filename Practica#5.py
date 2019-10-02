
age_born =  int(input("En que año naciste:"))
año_actual = int(input("En que año estamos? "))

age = año_actual - age_born

cumplidos = input("Ya los cumpliste?")
if (cumplidos == "si"):
    print(age)
elif (cumplidos == "no"):
    print(age - 1)
