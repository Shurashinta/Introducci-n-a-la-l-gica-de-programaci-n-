#  Pedir un número y decir si es par o impar.

# Entrada de datos
# Declarar
# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número: "))

# Salida de datos
# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
elif numero % 2 != 0:
    print(f"{numero} es un número impar.")