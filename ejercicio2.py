import random

# 1. Crear y llenar la matriz de 4x4 con enteros aleatorios entre 0 y 4
matriz = []
for _ in range(4):
    fila = []
    for _ in range(4):
        fila.append(random.randint(0, 4))
    matriz.append(fila)

# Definir las líneas divisorias del formato visual
linea_borde = "+---+---+---+---+"

# 2. Desplegar el resultado con el formato solicitado
print(linea_borde)
for fila in matriz:
    celdas_formateadas = []
    for num in fila:
        # Si el número es 0, se muestra vacío; si no, se muestra el número
        if num == 0:
            celdas_formateadas.append(" ")
        else:
            celdas_formateadas.append(str(num))
    
    # Unir las celdas con barras verticales
    print(f"| {celdas_formateadas[0]} | {celdas_formateadas[1]} | {celdas_formateadas[2]} | {celdas_formateadas[3]} |")
    print(linea_borde)
