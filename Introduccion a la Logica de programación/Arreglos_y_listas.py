# Arreglos / Listas .- Variable que almacena una colección de datos de uno o distintos tipos de datos
# Sintaxis:

# nombre_de_la_variable = [valor1, valor2, valor3, ....]

# Declarar o crear una lista
nombres = ["Michelle", "Hugo", "Aarón", "Ignacio"]
# Indice:    0           1        2        3        index
edades = [20, 30, 40, 50]

# Operaciones con Arreglos / Listas

# Agregar o insertar un elemento en una lista
nombres.append("Eduardo")
edades.append(60)


# Eliminar un elemento en una lista
nombres.remove("Hugo")
edades.remove(30)

# Acceder o editar a un elemento en una lista
nombres[0] = "Miguel"
edades[0] = 25

# Obtener la longitud de una lista
nombres(len("Eduardo")) # lenght
edades(len(60))

# Ordenar una lista
nombres.sort()
edades.sort(reverse=True)

print("NOMBRE:", nombres)
print("EDADES:", edades)