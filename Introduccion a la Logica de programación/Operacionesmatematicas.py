# Operaciones matematicas (Suma, Resta, Multiplicación, División, Potencia, Raiz Cuadradaa, Modulo)
# Entrada de datos
numero1 = float(input("ingresa un numero:")) 
numero2 = float(input("ingresa un numero:"))

PI = 3.1416 # Declarar, crear o instanciar una constante


# Importar librerias
import math

# Procesos
suma = numero1 + numero2
resta = numero1 - numero2
multiplicación = numero1 * numero2
división = numero1 / numero2
potencia_1 = numero1 ** numero2
potencia_2 = pow(numero1, numero2)
cuadrado = numero1 ** 2
cubo = numero2 ** 3
raiz_cuadrada_1 = math.sqrt(27)
raiz_cuadrada_2 = pow(27, 1/2)
raiz_cúbica = pow(27, 1/3)
modulo_residuo = numero1 % numero2


# Salida de datos
print("la suma es =", suma)
print("la resta es =", resta)
print("la multiplicacion es =", multiplicación)
print("la division es =", round(división, 4))
print("la potencia es =", round(potencia_1, 6))
print("la potencia es =", round(potencia_2,5))
print("el cuadrado es =", cuadrado)
print("el cubo es =", cubo)
print("la raiz cuadrada es =", raiz_cuadrada_1)
print("la raiz cuadrada es =", raiz_cuadrada_2)
print("la raiz cúbica es =", raiz_cúbica)
print("el modulo es =", modulo_residuo)