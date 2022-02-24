import random
from variables import FILAS, COLUMNAS, DISPAROS, BARCOS_INICIALES, MAR, BARCO, BARCO2, BARCO3, BARCO4, SUBMARINO, SUBMARINO2, SUBMARINO3, SUBMARINO_TOCHO, SUBMARINO_TOCHO2, CRUCERO, MAR, DISPARO_AL_AGUA, TOCADO, JUGADOR_1, JUGADOR_2

def oponente_de_jugador(jugador):
    if jugador == JUGADOR_1:
        return JUGADOR_2
    else:
        return JUGADOR_1

def matriz_vacia():
    matriz = []
    for x in range(FILAS):
        # Agregamos un arreglo a la matriz, que sería una fila básicamente
        matriz.append([])
        for y in range(COLUMNAS):
            # Y luego agregamos una celda a esa fila. Por defecto lleva "AGUA"
            matriz[x].append(MAR)
    return matriz

def imprimir_matriz(matriz, mostrar, jugador):
    print("Este es el tablero de " + str(jugador))
    numero = 1
    for y in range(FILAS):
        separador_horizontal()
        print(f"| {numero} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if not mostrar and valor_real != MAR and valor_real != DISPARO_AL_AGUA and valor_real != TOCADO:
                valor_real = " "
            print(f"| {valor_real} ", end="")
        numero = incrementar_numero(numero)
        print("|",)  # Salto de línea
    separador_horizontal()
    fila_de_numeros()
    separador_horizontal()


def incrementar_numero(numero):
    return numero+1


def separador_horizontal():
    for _ in range(COLUMNAS+1):
        print("----", end="")
    print("-")


def fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")


# Indica si una coordenada de la matriz está vacía
def es_agua(x, y, matriz):
    return matriz[y][x] == MAR


def coordenada_en_rango(x, y):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1


def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS-1)


def obtener_y_aleatoria():
    return random.randint(0, FILAS-1)


def colocar_barcos_de_una_celda(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        if es_agua(x, y, matriz):
            matriz[y][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_dos_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_agua(x, y, matriz) and es_agua(x2, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_dos_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y+1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_agua(x, y, matriz) and es_agua(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_tres_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x3 = x+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x3, y) and es_agua(x, y, matriz) and es_agua(x3, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x3] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz


def colocar_barcos_de_tres_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y3 = y+2
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y3) and es_agua(x, y, matriz) and es_agua(x, y3, matriz):
            matriz[y][x] = tipo_barco
            matriz[y3][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_cuatro_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x4 = x+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x4, y) and es_agua(x, y, matriz) and es_agua(x4, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x4] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos_de_cuatro_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y4 = y+3
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y4) and es_agua(x, y, matriz) and es_agua(x, y4, matriz):
            matriz[y][x] = tipo_barco
            matriz[y4][x] = tipo_barco
            barcos_colocados += 1
        if barcos_colocados >= cantidad:
            break
    return matriz

def colocar_barcos(matriz, cantidad_barcos, jugador):
    # Dividimos y redondeamos a entero hacia abajo (ya que no podemos colocar una parte no entera de un barco)
    barcos_una_celda = cantidad_barcos-6
    barcos_dos_celdas = cantidad_barcos-7
    barcos_tres_celdas = cantidad_barcos-8
    barcos_cuatro_celdas = cantidad_barcos-9
    if jugador == JUGADOR_1:
        print("Imprimiendo barcos del jugador 1 ")
    else:
        print("Imprimiendo barcos del jugador 2 ")
    print("Barcos de una celda: " +str(barcos_una_celda)+ "\nBarcos de dos celdas: " +str(barcos_dos_celdas)+ "\nBarcos de tres celdas: " +str(barcos_tres_celdas)+ "\nBarcos de cuatro celdas: " +str(barcos_cuatro_celdas)+ "\nTotal: " +str(barcos_una_celda+barcos_dos_celdas+barcos_tres_celdas+barcos_cuatro_celdas))
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, BARCO, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, BARCO2, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, BARCO3, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, BARCO4, matriz)
    matriz = colocar_barcos_de_dos_celdas_horizontal(barcos_dos_celdas, SUBMARINO, matriz)
    matriz = colocar_barcos_de_dos_celdas_horizontal(barcos_dos_celdas, SUBMARINO2, matriz)
    matriz = colocar_barcos_de_dos_celdas_vertical(barcos_dos_celdas, SUBMARINO3, matriz)
    matriz = colocar_barcos_de_tres_celdas_horizontal(barcos_tres_celdas, SUBMARINO_TOCHO, matriz)
    matriz = colocar_barcos_de_tres_celdas_vertical(barcos_tres_celdas, SUBMARINO_TOCHO2, matriz)
    matriz = colocar_barcos_de_cuatro_celdas_horizontal(barcos_cuatro_celdas, CRUCERO, matriz)
    return matriz

def imprimir_matrices_con_barcos(matriz_j1, matriz_j2):
    print("Mostrando ubicación de los barcos de ambos jugadores:")
    imprimir_matriz(matriz_j1, True, JUGADOR_1)
    imprimir_matriz(matriz_j2, True, JUGADOR_2)


def solicitar_coordenadas(jugador):
    print("Solicitando coordenadas de disparo al jugador " +str(jugador))
    y = None
    x = None
    while True:
        try:
            y = int(input("Ingresa el número de fila: "))
            if coordenada_en_rango(0, y-1):
                y = y-1
                break
            else:
                print("Fila inválida")
        except:
            print("Ingresa un número válido")
    # Hacemos lo mismo pero para la columna
    while True:
        try:
            x = int(input("Ingresa el número de columna: "))
            if coordenada_en_rango(x-1, 0):
                x = x-1
                break
            else:
                print("Columna inválida")
        except:
            print("Ingresa un número válido")

    return x, y

def disparar(x, y, matriz):
    if es_agua(x, y, matriz):
        matriz[y][x] = DISPARO_AL_AGUA
        return False
    # Si ya había disparado antes en esa coordenada, lo cuento como fallo igualmente
    elif matriz[y][x] == DISPARO_AL_AGUA or matriz[y][x] == TOCADO:
        return False
    else:
        matriz[y][x] = TOCADO
        return True

def imprimir_disparos_restantes(disparos_restantes, jugador):
    print("Disparos restantes de ", jugador, ": " ,disparos_restantes)

def indicar_victoria(jugador):
    print(f"Fin del juego\nEl jugador {jugador} es el ganador")


def indicar_fracaso(jugador):
    print(
        f"Fin del juego\nEl jugador {jugador} pierde. Se han acabado sus disparos")


def barcos_hundidos(matriz):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            # Si no es mar o un disparo, significa que todavía hay un barco por ahí
            if celda != MAR and celda != TOCADO and celda != DISPARO_AL_AGUA:
                return False
    return True
