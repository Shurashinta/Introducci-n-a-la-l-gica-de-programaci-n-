# Funciones, tareas que vamos a declarar
# Sintaxis
# ...
# def Nombre_de_la_función(parametros o argumentos):
#     instrucciones o procesos que va a realizar la funcion
#     return valor         (Se dice que vuelve, retorna o regresa un valor)
# ...
# Declarar o crear una funcion

def Saludar():
    print("Hola Mundo"); 

def Sumar(num1, num2):   # La funcion obtiene o recibe dos Parametros o argumentod
    return num1 + num2

def Restar(num1, num2):
    return num1 - num2

def Multiplicar(num1, num2):
    return num1 * num2

def Dividir(num1, num2):
    return num1 / num2

# Mandar a llamar o invocar una funcion para ejecutarla
print("**********Menu***********")
print("😆. Saludo")
print("2. Suma")
print("3. Resta")
print("4. multiplicación")
print("5. dividisión")
opción = int(input("ingresa una opcion: "))


if (opción  != 1):
    
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))

if (opción == 1):
    Saludar()

elif (opción == 2):
    print("La suma =", Sumar(num1, num2)) # Mando a llamar la función y le paso o enviar los parametros o argumentos

elif (opción == 3):
    print("La resta =", Restar(num1, num2))

elif (opción == 4):
    print("La multiplicación =", Multiplicar(num1, num2))

elif (opción == 5):
    print("La división =", Dividir(num1, num2))

else:
    print("opción no valida")
   