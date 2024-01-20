#  Pedir la cantidad de grados y convertirlos a °C, °F y K.

# Importar librerias o bibliotecas

# Entrada de datos
# Declarar
grados = float(input("Ingresa el número de grados:"))

# Procesos
celsius1 = grados - 273.15
fahrenheit1 = ((9 *(grados - 273.15)) / 5) + 32
celsius2 = (5 *(grados - 32))/ 9
kelvin1 = ((5 *(grados - 32))/ 9) + 273.15
kelvin2 = grados + 273.15
fahrenheit2 = ((9 * grados) / 5) +32


# Salida de datos
print ("Los grados son =", celsius1)
print ("los grados son =", fahrenheit1)
print ("los grados son =", celsius2)
print ("los grados son =", kelvin1)
print ("los grados son =", kelvin2)
print ("los grados son =", fahrenheit2)
