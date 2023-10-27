from Lista_preguntas import *
from funciones import *
from random import *
import pygame
from pygame.locals import *

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,155,255)
#tamaño pantalla
ANCHO = 1000
ALTO = 600


#Iniciamos pygame
pygame.init()
#Fondos
fondo = pygame.image.load(r"parcial-juego\imagenes\fondo.jpg")
fondo_game_over =pygame.image.load(r"parcial-juego\imagenes\game-over.jpg")
fondo = pygame.transform.scale(fondo,(ANCHO,ALTO))
fondo_game_over = pygame.transform.scale(fondo_game_over,(ANCHO,ALTO))
#Imagenes botones
boton_azul_imagen=pygame.image.load(r"parcial-juego\imagenes\boton-azul.png")
boton_azul_imagen = pygame.transform.scale(boton_azul_imagen,(70,70))
boton_rojo_imagen=pygame.image.load(r"parcial-juego\imagenes\boton-rojo.png")
boton_rojo_imagen = pygame.transform.scale(boton_rojo_imagen,(70,70))
#Titulo barra
pygame.display.set_caption("Esto o aquello!")
#Fuente
fuente = pygame.font.SysFont("Arial",30)
#Creamos la ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))
icono_barra = pygame.image.load(r"parcial-juego\imagenes\boton-azul.png")
pygame.display.set_icon(icono_barra)
#Insertamos el fondo
ventana.blit(fondo,(0,0))

#ventana.fill(fondo)


bandera = True
clickeado = False
puntaje=0
tiempo_final=0
clock = pygame.time.Clock()
tiempo_inicial = pygame.time.get_ticks()
while bandera:
    ventana.blit(boton_rojo_imagen,(250,400))
    ventana.blit(boton_azul_imagen,(500,400))

    pygame.display.update()
    cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
    ventana.blit(cartel,(155,50))
    user_answer=""
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido =tiempo_actual - tiempo_inicial
    tiempo_final =tiempo_transcurrido*0.001
    tiempo_impreso= fuente.render(f"Tiempo: {str(int(tiempo_final))}",True,ROJO,AZUL)
    ventana.blit(tiempo_impreso,(10,20))
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False 
        if event.type == pygame.KEYDOWN and user_answer =="" and tiempo_final <15:
            if event.key == pygame.K_RETURN and user_answer == "":
                ventana.blit(fondo,(0,0))
                puntos = fuente.render(f"Puntaje: {puntaje}",True,AZUL,ROJO)
                ventana.blit(puntos,(600,120))
                numero = numero_random(lista_preguntas)
                pregunta_elegida = elegir_pregunta(lista_preguntas,numero)
                #print(pregunta_elegida)
                pregunta_impresa = fuente.render(str(pregunta_elegida[0]),True,AZUL_CLARO,BLANCO)
                ventana.blit(pregunta_impresa,(100,200))
                valor_rojo = pregunta_elegida[3]
                valor_azul = pregunta_elegida[4]
                rojo_impreso = fuente.render(str(valor_rojo),True,BLANCO,ROJO)
                azul_impreso = fuente.render(str(valor_azul),True,BLANCO,AZUL)
                ventana.blit(rojo_impreso,(250,480))
                ventana.blit(azul_impreso,(500,480))
                pygame.display.update()
        #BOTON ROJO
        if event.type == pygame.MOUSEBUTTONDOWN and user_answer == "":
            try:
                x=event.pos[0]
                y=event.pos[1]
                if event.button == 1 and x >=240 and x <=300 and y>=400 and y<=450:
                    user_answer = "rojo"
                    clickeado = True
                    pygame.display.update()
            except:
                bandera = False
            if event.type == pygame.MOUSEBUTTONDOWN and user_answer =="":
                try:
                    x=event.pos[0]
                    y=event.pos[1]
                    if event.button == 1 and x >=490 and x <=550 and y >=390 and y<=450 :
                        user_answer = "azul"
                        clickeado= True
                        pygame.display.update()
                except:
                    bandera = False
        if clickeado == True and user_answer !="" and user_answer != str(pregunta_elegida[1] ) or tiempo_final > 15.00 :
            try:
                #finalizar = fuente.render("Perdiste \n Termino el juego",True,ROJO,AZUL)
                #ventana.blit(finalizar,(250,300))
                tiempo_final = 0
                ventana.blit(fondo_game_over,(0,0))
                puntos = fuente.render(f"Puntaje Final: {puntaje}",True,AZUL,ROJO)
                ventana.blit(puntos,(300,500))
                imprimir_pregunta = True
                pygame.mixer.music.load(r"parcial-juego\audios\incorrecto.mp3")
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(0.1)
                pygame.display.update()
            except:
                break
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 0:
            icono = pygame.image.load(r"parcial-juego\imagenes\cero_azules.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(350,100))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer = ""
            puntaje = puntaje + 10
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)
            print(puntaje)
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 20:
            icono = pygame.image.load(r"parcial-juego\imagenes\uno_azul.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(350,100))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer = ""
            puntaje = puntaje + 10
            print(puntaje)
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 40:
            icono = pygame.image.load(r"parcial-juego\imagenes\dos_azules.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(350,100))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer = ""
            puntaje = puntaje + 10
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 60:
            icono = pygame.image.load(r"parcial-juego\imagenes\tres_azules.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(350,100))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer = ""
            puntaje = puntaje + 10
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 80:
            icono = pygame.image.load(r"parcial-juego\imagenes\cuatro_azules.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(351,101))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer=""
            puntaje = puntaje + 10
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.1)
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 100:
            icono = pygame.image.load(r"parcial-juego\imagenes\cinco_azules.png")
            icono_final = pygame.transform.scale(icono,(100,50))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(351,101))
            ventana.blit(icono_final,(250,100))#(x,y)
            imprimir_pregunta = True
            user_answer = ""
            puntaje = puntaje + 10
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.2)
            pygame.display.update()
    
pygame.display.update()
pygame.quit()
