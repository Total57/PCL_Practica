
print("\nEste programa calculará el promedio de tus calificaciones")

materias = ["Matemáticas", "Español", "Historia", "Ingles", "Computación", "Socioemocional", "Química"]
calificaciones = []

for i in materias:
    cal = int(input("\nDigita tu calificación en " + i + ": "))
    calificaciones.append(cal)

suma = 0
for calificaciones in calificaciones:
    suma += calificaciones

promedio = suma / len(materias)
print("\nTu promedio es:", round(promedio, 2))

if promedio >= 6:
    if promedio >= 9:
        print("Bien hecho sigue asi ")
    if promedio >=8 and promedio < 9:
        print("No esta mal pero puedes hacerlo mejor")
    if promedio >=7 and promedio < 8:
        promedio("Bien, pasaste pero esfuerzate más a la próxima")
    if promedio >=6 and promedio < 8:
        promedio("Apenas y pasaste, debes esforrzarte más")
else:
    print("\nEstas Reprobado :(")







