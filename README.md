# Hundir La Flota

![hundir](https://user-images.githubusercontent.com/98879159/164447948-7fb670d2-218f-4fb2-84e1-fa8352291df7.png)

## ¿Qué es?

He creado mi propio juego de **Hundir la flota** en Python.

## ¿Cómo funciona el juego?

1. Hay dos jugadores: la máquina y tú
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. 
4. Los barcos son:
    - 4 barcos de 1 posición de eslora
    - 3 barcos de 2 posiciones de eslora
    - 2 barcos de 3 posiciones de eslora
    - 1 barco de 4 posiciones de eslora
5. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
6. Funciona por turnos y empiezas tú.
7. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
8. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
9. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.

