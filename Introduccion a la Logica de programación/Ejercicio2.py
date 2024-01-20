# Calcular el área y perímetro de un círculo.

# Importar librerias o bibliotecas 

# Entrada
PI = 3.1416 
radio = float(input("Ingresa el tamaño del radio: ")) 

# Proceso
perimetro = 2 * PI * radio
area = PI * radio ** 2


# Salida
print ("El perímetro es =", round(perimetro, 2))
print ("El área es =", round(area, 2))