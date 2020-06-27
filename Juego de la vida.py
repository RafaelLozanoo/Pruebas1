import pygame #Libreria usada para programar juegos en python
import numpy as np #Matrices y funciones matematicas

pygame.init() #Se crea la pantalla del juego

#Se establece el ancho y largo de la pantalla del juego
width, heigth =500, 500
screen = pygame.display.set_mode((heigth, width))
#Color del fondo
bg = 25,25, 25
#Rellena el fondo con el color elegido
screen.fill(bg)
#Numero de celdas
nxC, nyC =25,25
#Dimensiones de la celda
dimCW = width / nxC
dimCH = heigth / nyC
#Estado de las celdas, Vivas=1; Muertas=0
gameState = np.zeros((nxC,nxC))



#Bucle de ejecucion para que la pantalla permanezca
while True :
    for y in range(0, nxC):
        for x in range (0, nyC):

            #Calculamos el numero de vecinos cercanos
            n_vec = gameState[(x-1) % nxC, (y-1) % nyC]  + \
                    gameState[(x)   % nxC, (y-1) % nyC]  + \
                    gameState[(x+1) % nxC, (y-1) % nyC]  + \
                    gameState[(x-1) % nxC, (y)   % nyC]  + \
                    gameState[(x+1) % nxC, (y)   % nyC]  + \
                    gameState[(x-1) % nxC, (y+1) % nyC]  + \
                    gameState[(x)   % nxC, (y+1) % nyC]  + \
                    gameState[(x+1) % nxC, (y+1) % nyC]

#Reglas
#Regla #1: Una celula muerta con exactamente 3 vecicas vivas, "Revive"
if gameState[x,y] ==0 and n_vec ==3:
    gameState[x,y]=1
#Regla #2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "Muerta"
elif gameState[x,y] == 1 and (n_vec < 2 or n_vec >3):
    gameState[x,y] == 0

#Creamos el polygono de cada celda a dibujar
            poly= [((x)* dimCW, y* dimCH),
            ((x+1)* dimCW, y * dimCH),
            ((x+1)* dimCW, (y+1)*dimCH),
            ((x)* dimCW, (y+1) * dimCH)]
#Dibujamos la celda para cada par de x e y
            pygame.draw.poligon(screen, (128, 128, 128),poly,1)

            pygame.display.flip()

    pass
