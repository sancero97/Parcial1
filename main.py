def averageStudent():
    average = 0
    for j in range(1,5):
        average = average + float(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average

numAlumnos = 0
students = []
countWomenSoftware = 0
countMenSoftware = 0
countNotBinarySoftware = 0
countWomenTelecomunications = 0
countMenTelecomunications = 0
countNotBinaryTelecomunications = 0
averageTelecomunications = 0
averageSoftware = 0
countStudents = 0
averageAge = 0
countWomen = 0
countMen = 0
menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri)  ")
if menu == "admi":
    numAlumnos = int(input("Ingrese número de alumnos"))
    for i in range(numAlumnos):
        name = input("Ingrese nombre")
        
            countStudents = 0

            while True:
            name = input("Ingrese nombre")
            academicProgram = input("Ingrese programa académico -> s - software - t - telecomunicaciones") 
            students.append({"name": name, "academicProgram": academicProgram}) 
            stopProgram = input("Desea parar el programa (s - si, otra tecla continuar)")
            if stopProgram == "s" or stopProgram == "S":
               break


            for i in range(len(academicProgram)):
            print(f"{i + 1}: El estudiante {academicProgram[i]['name']} escogio el programa: {academicProgram[i]['programa']}")

     

    
    averageSoftware = averageSoftware/(countMenSoftware+countNotBinarySoftware+countWomenSoftware)  
    averageTelecomunications = averageTelecomunications/(countMenTelecomunications+countNotBinaryTelecomunications+countWomenTelecomunications)
    print(f"Promedio Software: {averageSoftware}")
    print(f"Número de mujeres en Software: {countWomenSoftware}")
    print(f"Número de Hombres en Software: {countMenSoftware}")
    print(f"Número de no binarios en Software: {countNotBinarySoftware}")
    print(f"Promedio Telecomunicaciones: {averageTelecomunications}")
    print(f"Número de mujeres en Telecomunicaciones: {countWomenTelecomunications}")
    print(f"Número de Hombres en Telecomunicaciones: {countMenTelecomunications}")
    print(f"Número de no binarios en Telecomunicaciones: {countNotBinaryTelecomunications}")
    for i in students:
        print(f"Nombre: {i['name']} - Nota final: {i['average']}")

else:
    while True:
        average+=int(input("Ingrese edad"))
        sex = input("Ingrese sexo")
        if sex == "m" or sex == "M":
            countWomen+=1
        elif sex == "h" or sex == "H":
            countMen+=1
        stopAdmission = input("si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar")
        countStudents+=1
        if stopAdmission == 0:
            break

    averageAge = averageAge/countStudents
    print(f"Número de estudiantes matriculados: {countStudents}")
    print(f"Promedio de edad de matriculados: {averageAge}")
    print(f"Número de mujeres matriculadas: {countWomen}")
    print(f"Número de hombres matriculados: {countMen}")
