# Evaluación
#     Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, muestre su resultado aciertos / 12 y mostrar el calificación = (aciertos / 12) * 10:

# Entreda
aciertos = 0

# Prosedimiento
aciertos = aciertos + 1  # // variable acumulador
aciertos += 1 # // abreviada

# (decrementar = aciertos - 1) 

# Respuesta
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.")
print("a) IDE b) Pseudocódigo c) Compilador d) ANSI / ISO")
respuesta = input()
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
       
print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
print(" a) Información     b) Datos     c) Programa     d) Código")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
      
print("3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.")
print("a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode")
respuesta = input()
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
  
print("4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.")
print("( a) Proceso     b) Solución     c) Función     d) Algoritmo)")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
    
print("5. Conjunto de elementos que se relacionan para cumplir una función determinada.")
print("a) Estructura     b) Datos     c) Operación     d) Sistema")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
       
print("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.")
print("a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
       
print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor.")
print("a) Constante     b) Variable     c) Librería     d) Tipo de Dato")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
        
print("8. Conjunto de símbolos, letras, números que no tienen un significado.")
print("a) Datos     b) Estructura     c) Información     d) Sistema")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
       
print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")
print("a) Filosofía     b) Sociología     c) Lógica     d) Argumentación")
respuesta = input("Marca la opción correcta")
if (respuesta == "c"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
   
print("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.")
print("a) Evento     b) Estándar     c) Calidad     d) Productividad")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
    
print("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.")
print("a) Estructura     b) Sistema     c) Objeto     d) Virtual")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
      
print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.")
print("a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando")
respuesta = input("Marca la opción correcta")
if (respuesta == "b"):
        print("Correcto")
        aciertos = aciertos + 1
else:
        print("Incorrecto")
    
aciertos / 12 
calificación = (aciertos/12)*10



# Salida
