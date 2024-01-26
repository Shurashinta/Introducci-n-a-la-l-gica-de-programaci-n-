# Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendo su pago por día de $250.-

# Importar librerias o bibliotecas

# Entrada de datos
# Declarar
ingresa_el_mes = input ("Ingresa el mes")
sueldo_por_día = float(input("Ingresar el sueldo por día: "))
días_laborados = float(input("ingresar los días que van a laborara: "))


# Procesos

pago_bruto = (sueldo_por_día * días_laborados)
iva_trasladado = (pago_bruto * 0.16)
sub_total = (pago_bruto + iva_trasladado)
iva_retenido = 2/3*iva_trasladado
isr_retenido = (sub_total * 0.10)
sueldo_neto = (sub_total - iva_retenido - isr_retenido)


# Salida de datos
print ("El sueldo neto es: ", sueldo_neto)



