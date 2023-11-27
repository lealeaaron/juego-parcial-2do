from creador_plataformas import *
from configuraciones import *
from class_personaje import *
from pygame.locals import *
from class_enemigo import *
from modo import *
from lvl_1 import *
from lvl_2 import *
from lvl_3 import *
from selector_niveles import *
import sys




##############################INICIALIZACIONES##########################################

#############Pantalla##########
ANCHO, ALTO = 1600 , 900
FPS = 28 #para desacelerar la pantalla

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO, ALTO)) # en pixeles

#Fondo
fondo = pygame.image.load(r"Recursos\fondo.png")#Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO)) 

piso_textura = pygame.image.load(r"Recursos\piso.png")
piso_textura = pygame.transform.scale(piso_textura, (ANCHO, ALTO))



#Personaje
diccionario_animaciones = {}
diccionario_animaciones["derecha"] = jugador_derecha
diccionario_animaciones["quieto"] = jugador_quieto
diccionario_animaciones["quietoizquierda"] = jugador_quieto_izquierda
diccionario_animaciones["izquierda"] = jugador_izquierda
diccionario_animaciones["salta"] = jugador_salta
diccionario_animaciones["saltaizquierda"] = jugador_salta_izquierda

###############################  Personaje y Piso  ###################################

jugador = Personaje(diccionario_animaciones,500,160,(70,60), 9, "quieto") #le pasa los atributos al class_personaje

piso = crear_plataforma(False, (ANCHO,20), (0,825))


##################  pone al jugador en el piso   #####################



jugador.hitbox.bottom = piso["rectangulo"].top


###############################  ENEMIGO  ###############################


#diccionario_animaciones_enemigo = {"izquierda": enemigo_camina, "aplastado": enemigo_aplastado }
#un_enemigo =  Enemigo(diccionario_animaciones_enemigo)

#un_enemigo.rectangulo.bottom = piso["rectangulo"].top

#lista_enemigos = [un_enemigo]


######################### LOOP DEL JUEGO ##########################

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False
        elif evento.type == KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == MOUSEBUTTONDOWN:
            print(evento.pos)
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        jugador.que_hace = "derecha"
        #direccion es derecha
    elif teclas[pygame.K_LEFT]:
        jugador.que_hace = "izquierda"
        #direccion es izquierda
    elif jugador.izquierda == True:
        jugador.que_hace = "quietoizquierda"
    else:
        jugador.que_hace = "quieto"



    if teclas[pygame.K_UP]:
        if jugador.izquierda == True:
            jugador.que_hace = "saltaizquierda"
        else:
            jugador.que_hace = "salta"



    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(piso_textura,(0,821))


    if lvl_1 == True:
        jugador.actualizar(PANTALLA,lista_plataformas_lvl_1)
    elif lvl_2 == True:
        jugador.actualizar(PANTALLA,lista_plataformas_lvl_2)
    else:
        jugador.actualizar(PANTALLA,lista_plataformas_lvl_3)

        
    Personaje.metodo_estatico()

    #un_enemigo.actualizar(PANTALLA)
    
    #mario.verificar_colision_enemigo(un_enemigo)
    
    #for enemigo in lista_enemigos:
    #    if enemigo.esta_muerto:
    #        del enemigo

    if obtener_modo():
        pygame.draw.rect(PANTALLA, "pink", jugador.hitbox, 3)
        if lvl_1 == True:
            for plataforma in lista_plataformas_lvl_1:
                pygame.draw.rect(PANTALLA, "red",plataforma["rectangulo"] , 3)
        elif lvl_2 == True:
            for plataforma in lista_plataformas_lvl_2:
                pygame.draw.rect(PANTALLA, "red",plataforma["rectangulo"] , 3)
        else:
            for plataforma in lista_plataformas_lvl_3:
                pygame.draw.rect(PANTALLA, "red",plataforma["rectangulo"] , 3)

    pygame.display.update()

pygame.quit()


