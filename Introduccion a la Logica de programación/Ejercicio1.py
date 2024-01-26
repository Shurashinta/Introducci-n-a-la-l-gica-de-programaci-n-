# Ejercicio 1 Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.


# Importar librerias o bibliotecas

# Entrada de datos
# Declarar
calificación_1 = float(input("Ingresa la primera calificación: "))
calificación_2 = float(input("Ingresa la segunda calificación: "))
calificación_3 = float(input("Ingresa la tercera calificación: "))

# Procesos
# Jerarquia de operadores
# Potencia y raiz
# multiplicacion y división
# suma y resta
promedio = (calificación_1 + calificación_2 + calificación_3) / 3 

# Salida de datos
print ("El promedio es =", round(promedio, 2))

# Determinar si el estudiante aprobó o reprobó
if (promedio > 6 and promedio <= 10):
    print("Aprobado.")
elif (promedio == 6):
    print("Apenas aprobado")
elif (promedio >= 0 and promedio < 6):
    print("Reprobado")
elif (promedio < 0 or promedio > 10):
    print("Error")