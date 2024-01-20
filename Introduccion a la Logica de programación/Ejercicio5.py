# Obtener valores para: a, b y c. Calcular la fórmula general.

# Importar librerias o bibliotecas
import math

# Entrada de datos
# Declarar
a = float(input("Ingresa el número de a:")) 
b = float(input("Ingresa el número de b:"))
c = float(input("Ingresa el número de c:"))

# Procesos
x1 = (-b -math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a) 
x2 = (-b +math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)


# Salida de datos
print ("x1 =", x1)
print ("X2 =", x2)
