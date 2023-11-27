from configuraciones import *
from class_enemigo import *
from lvl_1 import *
from lvl_2 import *
from lvl_3 import *
from selector_niveles import *
class Personaje:
    def __init__(self, animaciones, pos_x, pos_y, tamaño, velocidad, que_hace):
        self.hitbox = pygame.Rect(pos_x, pos_y, *tamaño)
        self.hitbox.x = pos_x
        self.hitbox.y = pos_y
        
        #movimiento
        velocidad = 9
        self.velocidad = velocidad
        self.que_hace = que_hace
        self.contador_pasos = 0

        #animaciones
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.animacion_actual = self.animaciones[self.que_hace]

        #salto y gravedad 
        self.gravedad = 1
        self.desplazamiento_y = 0
        self.desplazamiento_x = 0
        self.potencia_salto = -15
        self.limite_velocidad_salto = 10
        self.esta_saltando = False
        self.animacion_saltando = False
        #se necesita una bandera de direccion!!!
        self.izquierda = False

        #colisiones
        self.in_air = True

###################### Gravedad ########################

    def aplicar_gravedad(self): 
        self.desplazamiento_y += self.gravedad
        self.hitbox.y += self.desplazamiento_y
        if self.desplazamiento_y >= 1:
            self.animacion_saltando = True


############################ Colisiones ###############################

    def colisiones_horizontales(self,lista_plataformas):
        for plataforma in lista_plataformas:
            if self.hitbox.colliderect(plataforma["rectangulo"]):
                if self.desplazamiento_x > 0:
                    self.hitbox.right = plataforma["rectangulo"].left
                elif self.desplazamiento_x < 0:
                    self.hitbox.left = plataforma["rectangulo"].right

    def colisiones_verticales(self,lista_plataformas):
        self.aplicar_gravedad()
        for plataforma in lista_plataformas:
            if self.hitbox.colliderect(plataforma["rectangulo"]):
                if self.desplazamiento_y > 0:
                    self.hitbox.bottom = plataforma["rectangulo"].top
                    self.desplazamiento_y = 0
                elif self.desplazamiento_y < 0:
                    self.hitbox.top = plataforma["rectangulo"].bottom
                    self.desplazamiento_y = 0
                if self.hitbox.bottom == plataforma["rectangulo"].top:
                    self.animacion_saltando = False



########################## Metodo Estatico ##########################
    @staticmethod
    def metodo_estatico():
        pass


    def desplazar(self):
        self.desplazamiento_x = self.velocidad
        if self.que_hace == "izquierda":
            self.desplazamiento_x *= -1

        self.hitbox.x += self.desplazamiento_x

    def saltar(self):
        if self.esta_saltando == True:
            self.desplazamiento_y = self.potencia_salto
            self.esta_saltando = False


    def animar(self,pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(self.animacion_actual[self.contador_pasos],self.hitbox)
        self.contador_pasos += 1


    def actualizar(self, pantalla,lista_plataformas):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(pantalla)
                    self.izquierda = False
                self.desplazar()
            case "izquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(pantalla)
                    self.izquierda = True
                self.desplazar()
            case "quieto":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["quieto"]
                    self.animar(pantalla)
            case "quietoizquierda":
                if not self.esta_saltando:
                    self.animacion_actual = self.animaciones["quietoizquierda"]
                    self.animar(pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.animacion_actual = self.animaciones["salta"]
                    self.animar(pantalla)
                self.saltar()
            case "saltaizquierda":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.animacion_actual = self.animaciones["saltaizquierda"]
                    self.animar(pantalla)
                self.saltar()
        

        if lvl_1 == True:
            lista_plataformas = lista_plataformas_lvl_1 
            self.colisiones_horizontales(lista_plataformas)
            self.colisiones_verticales(lista_plataformas)
        elif lvl_2 == True:
            lista_plataformas = lista_plataformas_lvl_2 
            self.colisiones_horizontales(lista_plataformas)
            self.colisiones_verticales(lista_plataformas)
        elif lvl_3 == True:
            lista_plataformas = lista_plataformas_lvl_3 
            self.colisiones_horizontales(lista_plataformas)
            self.colisiones_verticales(lista_plataformas)
        






    def verificar_colision_enemigo(self, enemigo:Enemigo):
        if self.hitbox.colliderect(enemigo.rectangulo):
            enemigo.esta_muerto = True





