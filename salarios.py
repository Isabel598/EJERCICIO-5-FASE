# ==========================================
# REPORTE DE TRABAJO SEMANAL
# ==========================================

# MATRIZ PRINCIPAL
matriz_empleados = []

# Dias laborables
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# ==========================================
# FUNCION PARA CALCULAR HORAS
# ==========================================

def calcular_horas(datos_empleado):

    nombre = datos_empleado[0]

    horas = datos_empleado[1:]

    total_horas = sum(horas)

    # Clasificacion
    if total_horas > 40:
        estado = "SobreTiempo"
    else:
        estado = "Horario Estandar"

    return nombre, total_horas, estado

# ==========================================
# INGRESO DE DATOS
# ==========================================

cantidad = int(input("Cuantos empleados desea registrar?: "))

for i in range(cantidad):

    print("\nDatos del empleado No", i + 1)

    nombre = input("Nombre: ")

    horas_semana = []

    print(">>Horas trabajadas en la semana:")

    for dia in dias:

        horas = int(input(f">> Cuanto trabajo el {dia}? "))

        horas_semana.append(horas)

    # Guardar datos en la matriz
    fila = [nombre] + horas_semana

    matriz_empleados.append(fila)

# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print("\n|----------------------------------------------------------|")
print("|    REPORTE DE TRABAJO SEMANAL DE LOS GRUPOS             |")
print("|----------------------------------------------------------|")
print("| Empleado        | Horas | Tipo de Jornada              |")
print("|----------------------------------------------------------|")

for empleado in matriz_empleados:

    nombre, total, estado = calcular_horas(empleado)

    print(f"| {nombre:<15} | {total:<6} | {estado:<28} |")

print("|----------------------------------------------------------|")
