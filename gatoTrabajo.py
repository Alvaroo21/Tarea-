tablero = [[' ' for _ in range(3)] for _ in range(3)]
jugador_actual = 'X'
juego_activo = True
movimientos = 0

while juego_activo:
    print("Tablero actual:")
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)
    
    fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (1, 2, 3): ")) - 1
    columna = int(input(f"Jugador {jugador_actual}, ingresa la columna (1, 2, 3): ")) - 1
    
    if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador_actual
        movimientos += 1
    else:
        print("Movimiento inválido. Intenta de nuevo.")
        continue
    
    ganador = False
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            ganador = True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            ganador = True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        ganador = True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        ganador = True
    
    if ganador:
        print(f"¡Jugador {jugador_actual} ha ganado!")
        juego_activo = False
    elif movimientos == 9:
        print("¡El juego es un empate!")
        juego_activo = False
    else:
        if jugador_actual == 'X':
            jugador_actual = 'O'
        else:
            jugador_actual = 'X'

print("Tablero final:")
for fila in tablero:
    print('|'.join(fila))
    print('-' * 5)
