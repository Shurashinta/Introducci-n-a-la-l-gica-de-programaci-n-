# 11. Pedir números enteros en un ciclo mientras sean positivos y en caso de
# que un número sea negativo cerrar el ciclo y al final promediar los
# números positivos ingresados por el usuario.

numero = float(input("Escribe un número: "))
sumatoria = 0 # Variable acumulador
contador = 0 # Variable contador

while(numero >= 0): # si el numero fue positivo
   # print(numero)
    sumatoria = sumatoria + numero
    contador = contador + 1
    numero = float(input("Escribe un número: "))

promedio = sumatoria / contador
print(promedio)
