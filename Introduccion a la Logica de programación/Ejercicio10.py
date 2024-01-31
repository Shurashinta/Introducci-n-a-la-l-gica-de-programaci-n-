#  10. Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido

num = int(input("ingresar valor: "))

if(num < 0 and num > -100):
    for i in range(-1, -101, -2): 
        print("Inpares", i)
if(num < 0 and num > -100):
    for i in range(-1, -99, 2):
        print("pares", i)
elif(num == 0 or num <= -100 or num >= 100):
    print("No valido")
if(num > 0 and num < 100):
    h = 0 
    while(h <= 100):
        print("Pares", h)
        h = h + 2
if(num > 0 and num < 100):
    h = 0 
    while(h <= 100):
        print("Novalidos", h)
        h = h + 3
