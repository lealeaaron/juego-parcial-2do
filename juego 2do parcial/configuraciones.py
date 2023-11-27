import pygame

def girar_imagenes(lista_original, flip_x, flip_y ): # para mario_izquierda y mario_chico_izquierda
    lista_girada = []
    
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


def reescalar_imagenes(diccionario_animaciones, tamaño):# se usa en los class
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)


######################## Jugador #########################


jugador_quieto = [pygame.image.load(r"recursos\quieto.png")]

jugador_quieto_izquierda = girar_imagenes(jugador_quieto, True, False)

jugador_derecha =  [pygame.image.load(r"recursos\camina 1.png"),
                    pygame.image.load(r"recursos\camina 2.png"),
                    pygame.image.load(r"recursos\camina 2.png"),
                    pygame.image.load(r"recursos\camina 3.png"),
                    pygame.image.load(r"recursos\camina 3.png"),
                    pygame.image.load(r"recursos\camina 1.png")]

jugador_izquierda = girar_imagenes(jugador_derecha, True, False)

jugador_salta = [pygame.image.load(r"recursos\jugador salta.png")]

jugador_salta_izquierda = girar_imagenes(jugador_salta, True, False)

jugador_perdiendo = [pygame.image.load(r"recursos\jugador pierde.png")]


