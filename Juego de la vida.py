import pygame# Libreria usada para programar juegos en python
import numpy as np# Matrices y funciones matematicas
import time

pygame.init()# Se crea la pantalla del juego

# Se establece el ancho y largo de la pantalla del juego
width, heigth = 800, 800
screen = pygame.display.set_mode((heigth, width))
# Color del fondo
bg = 25, 25, 25
# Rellena el fondo con el color elegido
screen.fill(bg)
# Numero de celdas
nxC, nyC = 80, 80
# Dimensiones de la celda
dimCW = width/nxC
dimCH = heigth/nyC
# Estado de las celdas, Vivas = 1; Muertas = 0
gameState = np.zeros((nxC, nxC))

# Automata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[4, 5] = 1
# Automata Movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Control de la ejecucion del juego
pauseExect = False
# Bucle de ejecucion para que la pantalla permanezca
running = True
while True:
    pygame.event.get()
    pygame.event.pump()
    newGameState = np.copy(gameState)
screen.fill(bg)
time.sleep(0.1)

# Registramos eventos de teclado y raton
ev = pygame.event.get()
for event in ev: #Detectamos si se preciona una tecla
            if event.type == pygame.KEYDOWN:
                pauseExect = not pauseExect# Detectamos si se preciona el raton
mouseClick = pygame.mouse.get_pressed()
if sum(mouseClick) > 0:
        posX, posY = pygame.mouse.get_pos()
celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
newGameState[celX, celY] = not mouseClick[2]

for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

        #Calculamos el numero de vecinos cercanos
                n_vec = gameState[(x - 1) %nxC, (y - 1) %nyC] + \
                        gameState[(x) %nxC, (y - 1) %nyC] + \
                        gameState[(x + 1) %nxC, (y - 1) %nyC] + \
                        gameState[(x - 1) %nxC, (y) %nyC] + \
                        gameState[(x + 1) %nxC, (y) %nyC] + \
                        gameState[(x - 1) %nxC, (y + 1) %nyC] + \
                        gameState[(x) %nxC, (y + 1) %nyC] + \
                        gameState[(x + 1) %nxC, (y + 1) %nyC]

# Reglas# Regla #1: Una celula muerta con exactamente 3 vecicas vivas, "Revive"

if gameState[x,y] == 0 and n_vec == 3:
        newGameState[x, y] = 1# Regla #2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "Muerta"

elif gameState[x,y] == 1 and(n_vec < 2 or n_vec > 3):
        newGameState[x, y] == 0

# Creamos el polygono de cada celda a dibujar
poly = [((x) * dimCW, y * dimCH),
        ((x + 1) * dimCW, y * dimCH),
        ((x + 1) * dimCW, (y + 1) * dimCH),
        ((x) * dimCW, (y + 1) * dimCH)]
        
        # Dibujamos la celda para cada par de x e y
if newGameState[x, y] == 0:
    pygame.draw.poligon(screen, (128, 128, 128), poly, 1)
else :
        pygame.draw.poligon(screen, (255, 255, 255), poly, 0)# Actualizar el estado del juego
gameState = np.copy(newGameState)

# Actualizar la pantalla
pygame.display.flip()

