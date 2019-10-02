

total_nota = 0
i = 1

while (i <= 3):
    nota_Examen = int(input("Nota del examen: "))
    total_nota = (total_nota + nota_Examen)
    i = i + 1

total_nota = total_nota/3

if(total_nota >= 70):
    print("aprobado")
else:
    print("Reprobado")
