from variables import DISPAROS, JUGADOR_1, JUGADOR_2
from funciones import oponente_de_jugador, matriz_vacia, imprimir_matriz, imprimir_disparos_restantes, colocar_barcos, solicitar_coordenadas, disparar, barcos_hundidos, indicar_victoria, imprimir_matrices_con_barcos, indicar_fracaso


def jugar():
    disparos_restantes_j1 = DISPAROS
    disparos_restantes_j2 = DISPAROS
    cantidad_barcos = 5
    matriz_j1, matriz_j2 = matriz_vacia(), matriz_vacia()
    matriz_j1 = colocar_barcos(
        matriz_j1, cantidad_barcos, JUGADOR_1)
    matriz_j2 = colocar_barcos(
        matriz_j2, cantidad_barcos, JUGADOR_2)
    turno_actual = JUGADOR_1
    print("===============")
    while True:
        print(f"Turno de {turno_actual}")
        disparos_restantes = disparos_restantes_j2
        if turno_actual == JUGADOR_1:
            disparos_restantes = disparos_restantes_j1
        imprimir_disparos_restantes(disparos_restantes, turno_actual)
        matriz_oponente = matriz_j1
        if turno_actual == JUGADOR_1:
            matriz_oponente = matriz_j2
        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        x, y = solicitar_coordenadas(turno_actual)
        acertado = disparar(x, y, matriz_oponente)
        if turno_actual == JUGADOR_1:
            disparos_restantes_j1 -= 1
        else:
            disparos_restantes_j2 -= 1

        imprimir_matriz(matriz_oponente, False,
                        oponente_de_jugador(turno_actual))
        if acertado:
            print("Disparo acertado")
            if barcos_hundidos(matriz_oponente):
                indicar_victoria(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
        else:
            print("Disparo fallado")
            if disparos_restantes-1 <= 0:
                indicar_fracaso(turno_actual)
                imprimir_matrices_con_barcos(matriz_j1, matriz_j2)
                break
            turno_actual = oponente_de_jugador(turno_actual)