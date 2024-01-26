# 9.- Realizar un Menú de Opciones y realizar una función para cada opción: (https://apps.timwhitlock.info/emoji/tables/unicode)
# ******** MENÚ *********
# a) Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación
# b) Calcular la nómina de un empleado en ENERO del 2024
# c) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
# d) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos


import secrets
import string

def generar_contrasena():
    longitud = 5
    caracteres = string.ascii_letters + string.digits  # letras mayúsculas, minúsculas y dígitos

    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena



# Procesos





def Mostrar():
    print ("Pon el nombre de una app de automoviles: ")

def Calcular():
    sueldo_por_día = int(input("Ingresar el sueldo por día: "))
    días_laborados = int(input("ingresar los días que van a laborara: "))
    pago_bruto = (sueldo_por_día * días_laborados)
    iva_trasladado = (pago_bruto * 0.16)
    sub_total = (pago_bruto + iva_trasladado)
    iva_retenido = 2/3*iva_trasladado
    isr_retenido = (sub_total * 0.10)
    sueldo_neto = (sub_total - iva_retenido - isr_retenido)
    print ("El sueldo neto es: ", round(sueldo_neto))

def Generar():
    longitud = 1 <= 5
    caracteres = string.ascii_letters + string.digits  # letras mayúsculas, minúsculas y dígitos

    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    if len(contrasena) != longitud:
        raise ValueError("Error: La contraseña generada no tiene la longitud esperada.")
    
    
    print ("Generar una contraseña con un numero de 5 caracteres: ", contrasena)

def Pedir():
    nombre = input("Escriba su nombre: ")
    primer_apellido = input("Escriba su primer apellido: ")
    segundo_apellido = input("Escriba su segundo apellido: ")
    edad = int(input("Escriba su edad: "))
    print ("Datos del usuario")
    print (nombre, primer_apellido, segundo_apellido, edad)

print("******** MENÚ *********")
print("1. Mostrar una lista de 3 servicios de pasaje con sus estrellas de calificación")
print("2. Calcular la nómina de un empleado en ENERO del 2024")
print("3. Genere una contraseña de 1 a 5 caracteres: ")
print("4. Datos del usuario: ")

opción = int(input("ingresa una opcion: "))


if (opción == 1):
    Mostrar()

elif (opción == 2):
    Calcular() # Mando a llamar la función y le paso o enviar los parametros o argumentos

elif (opción == 3):
   Generar()

elif (opción == 4):
    Pedir()

else:
    print("opción no valida")
