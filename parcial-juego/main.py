#Importamos pygame, la lista de preguntas, las funciones y la libreria random.
from Lista_preguntas import *
from funciones import *
from random import *
import csv
import pygame
import re
from pygame.locals import *

#colores asignados a variables.
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

lista_puntajes = leer_lista_puntajes()
ultimo_puntaje = str(lista_puntajes[0])





#Fondos
fondo = pygame.image.load(r"parcial-juego\imagenes\fondo.jpg")#cargamos la imagen.
fondo_game_over =pygame.image.load(r"parcial-juego\imagenes\game-over.jpg")
fondo = pygame.transform.scale(fondo,(ANCHO,ALTO))#Escalamos la imagen para que ocupe el ancho y el alto de la pantalla.
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
pygame.display.set_icon(icono_barra)#Cargamos el logo de la barra.
#Insertamos el fondo
ventana.blit(fondo,(0,0))


#Inicializamos las variables que vamos a usar.
bandera = True
bandera_juego_terminado= False
bandera_iniciar_juego = False
clickeado = False
bandera_ya_contesto = False
comodin_next_usado = False
comodin_half_usado = False
comodin_reload_usado = False
puntaje=0
tiempo_final=0
user_answer = ""
#lista_puntajes = []

tiempo_inicial = pygame.time.get_ticks()#Tiempo en milisegundos desde que iniciamos pygame

while bandera:#Se ejecuta el juego mientras la bandera esta en estado True.
    if bandera_iniciar_juego == False:#Si la bandera de iniciar juego esta en False...
        texto_iniciar_juego = fuente.render("Presiona la tecla enter para iniciar el juego",True,BLANCO,AZUL)
        robot_feliz = pygame.image.load(r"parcial-juego\imagenes\robot.png")
        robot_feliz = pygame.transform.scale(robot_feliz,(170,220))
        ventana.blit(robot_feliz,(50,150))
        ventana.blit(texto_iniciar_juego,(300,200))#Imprimimos el texto y la imagen en la pantalla. 
        ultimo_puntaje_texto = fuente.render(f"ultimo puntaje {ultimo_puntaje}",True,BLANCO,AZUL)
        ventana.blit(ultimo_puntaje_texto,(50,80))
        pygame.display.update()#Actualizamos la pantalla.
    if bandera_juego_terminado == False and bandera_iniciar_juego == True: #Si el juego no termino y el juego empezo...
        pygame.display.update()#Actualizamos la pantalla.
        user_answer=""#La respuesta del usuario toma un string vacio.
        tiempo_actual = pygame.time.get_ticks()#Tiempo en milisegundos desde que iniciamos el juego.
        tiempo_transcurrido =tiempo_actual - tiempo_inicial# calculamos el tiempo transcurrido.
        tiempo_final =tiempo_transcurrido*0.001 # Convertimos el tiempo de milisegundos a segundos.
        tiempo_impreso= fuente.render(f"Tiempo: {str(int(tiempo_final))}",True,ROJO,AZUL)#Renderizamos el tiempo en formato string.
        ventana.blit(tiempo_impreso,(10,20))#Imprimimos en la pantalla el tiempo.
    for event in pygame.event.get():#Detectamos los eventos realizados.
        if event.type == pygame.QUIT: #Si se presiona la cruz de arriba a la derecha...
            bandera = False #La bandera pasa a un estado False, el while deja de iterar el codigo y se cierra la ventana.
        if event.type == pygame.KEYDOWN and user_answer =="" and tiempo_final <15 : #Si se presiona una tecla, si el tiempo no supera los 15 segundos y el usuario no dio una respuesta...
            if event.key == pygame.K_RETURN and user_answer == "": #Si la tecla presionada es la tecla enter y el usuario no dio respuesta...
                tiempo_final = 0 # Se restablece el tiempo
                ventana.blit(fondo,(0,0))#Imprimimos el fondo.
                puntos = fuente.render(f"Puntaje: {puntaje}",True,AZUL,ROJO)
                ventana.blit(puntos,(600,120))#Imprimimos el puntaje.
                numero = numero_random(lista_preguntas)# obtenemos un numero random de la lista de preguntas a traves de la funcion (numero_random).
                pregunta_elegida = elegir_pregunta(lista_preguntas,numero)# A traves de la funcion (elegir_pregunta) obtenemos una pregunta random.
                print(pregunta_elegida)
                pregunta_impresa = fuente.render(str(pregunta_elegida[0]),True,AZUL_CLARO,BLANCO)#Renderizamos el primer valor de la lista que obtuvimos, el cual este seria una pregunta.
                ventana.blit(pregunta_impresa,(100,200))#Imprimimos la pregunta.
                valor_rojo = pregunta_elegida[3]#Asignamos el valor de la respuesta de color rojo.
                valor_azul = pregunta_elegida[4]#Asignamos el valor de la respuesta de color Azul.
                rojo_impreso = fuente.render(str(valor_rojo),True,BLANCO,ROJO)
                azul_impreso = fuente.render(str(valor_azul),True,BLANCO,AZUL)
                #Imprimimos los botones.
                ventana.blit(rojo_impreso,(250,400))
                ventana.blit(azul_impreso,(500,400))
                ventana.blit(boton_rojo_imagen,(250,320))
                ventana.blit(boton_azul_imagen,(500,320))
                boton_next = pygame.image.load(r"parcial-juego\imagenes\next.png")
                boton_next = pygame.transform.scale(boton_next, (60,60))
                boton_half = pygame.image.load(r"parcial-juego\imagenes\half.png")
                boton_half = pygame.transform.scale(boton_half,(60,60))
                boton_reload = pygame.image.load(r"parcial-juego\imagenes\reload.png")
                boton_reload = pygame.transform.scale(boton_reload,(60,60))
                texto_next = fuente.render("Next",True,BLANCO,NEGRO)
                texto_half = fuente.render("Half",True,BLANCO,NEGRO)
                texto_reload = fuente.render("Reload",True,BLANCO,NEGRO)
                #Los botones de los comodines solo se imprimen si no fueron usados.
                if comodin_next_usado == False:
                    ventana.blit(texto_next,(650,550))
                    ventana.blit(boton_next,(650,470))
                if comodin_half_usado == False:
                    ventana.blit(boton_half,(750,470))
                    ventana.blit(texto_half,(750,550))
                if comodin_reload_usado == False:
                    ventana.blit(boton_reload,(850,470))
                    ventana.blit(texto_reload,(850,550))
                pygame.display.update()
            
                bandera_iniciar_juego = True #Cambiamos la variable a un estado True para indicar que el juego inicio.
        #BOTON ROJO
        if event.type == pygame.MOUSEBUTTONDOWN and user_answer == "":#Si recibe un evento de que se hizo click y el usuario no dio respuesta...
            try:
                x=event.pos[0]#Se obtiene la posicion x.
                y=event.pos[1]#Se obtiene la posicion y.
                if event.button == 1 and x >=240 and x <=300 and y>=320 and y<=370:#Si se clickea en la zona donde esta ubicado el boton rojo...
                    user_answer = "rojo" #La respuesta del usuario es rojo.
                    clickeado = True #Marcamos que el usuario hizo click.
                    pygame.display.update()#Actualizamos la pantalla.
            except :#Si hay un error en tiempo de ejecucion...
                break #Detiene la ejecucion
            if event.type == pygame.MOUSEBUTTONDOWN and user_answer =="":#Si recibe un evento de que se hizo click y el usuario no dio respuesta...
                try:
                    x=event.pos[0]#Se obtiene la posicion x.
                    y=event.pos[1]#Se obtiene la posicion y.
                    if event.button == 1 and x >=490 and x <=550 and y >=320 and y<=370 :#Si se clickea en la zona donde esta ubicado el boton azul...
                        user_answer = "azul"#La respuesta del usario es azul.
                        clickeado= True#Marcamos que el usuario hizo click.
                        pygame.display.update()#Actualizamos la pantalla.
                except:#Detiene la ejecucion.
                    break#Detiene la ejecucion
                    
            if event.type == pygame.MOUSEBUTTONDOWN and user_answer =="" and comodin_next_usado == False:#Si recibe un evento de que se hizo click, el comodin (next) no fue usado y el usuario no dio respuesta...
                try:
                    x=event.pos[0]
                    y=event.pos[1]
                    if event.button == 1 and x >=650 and x <=710 and y >=470 and y<=530 :#Si se clickea en la zona donde esta ubicado el boton de comodin (next)...
                        user_answer = str(pregunta_elegida[1] )#Automaticamente da la respuesta correcta.
                        clickeado= True
                        comodin_next_usado = True#Marcamos que se uso el comodin para que no puede ser reutilizado.
                        
                except:#En caso de un error en tiempo de ejecucion...
                    break#Detiene la ejecucion.
            if event.type == pygame.MOUSEBUTTONDOWN and user_answer =="" and comodin_half_usado == False:#Si recibe un evento de que se hizo click, el comodin (half) no fue usado y el usuario no dio respuesta...
                try:
                    x=event.pos[0]
                    y=event.pos[1]
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 :#Si se clickea en la zona donde esta ubicado el boton de comodin (half)...
                        if int(pregunta_elegida[2]) == 0:#Si la cantidad de votantes azules es de cero...
                            pista = pygame.image.load(r"parcial-juego\imagenes\half_dos_rojos.png")
                            pista_final = pygame.transform.scale(pista,(200,100))
                            ventana.blit(pista_final,(300,250))#Imprimimos por pantalla dos muñecos rojos.
                            clickeado= True
                            comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                            
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 and int(pregunta_elegida[2]) == 20:#Si se clickea en la zona donde esta ubicado el boton de comodin (half) y la cantidad de votantes azules es de uno...
                        pista = pygame.image.load(r"parcial-juego\imagenes\half_uno_y_uno.png")
                        pista_final = pygame.transform.scale(pista,(200,100))
                        ventana.blit(pista_final,(300,250))#Imprimimos por pantalla un muñeco azul y un muñeco rojo.
                        clickeado= True
                        comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                        print("hola")
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 and int(pregunta_elegida[2]) == 40 :#Si se clickea en la zona donde esta ubicado el boton de comodin (half) y la cantidad de votantes azules es de dos...
                        pista = pygame.image.load(r"parcial-juego\imagenes\half_dos_rojos.png")#Imprimimos en pantalla dos muñecos rojos.
                        pista_final = pygame.transform.scale(pista,(200,100))
                        ventana.blit(pista_final,(300,250))
                        clickeado= True
                        comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 and int(pregunta_elegida[2]) == 60 :#Si se clickea en la zona donde esta ubicado el boton de comodin (half) y la cantidad de votantes azules es de tres...
                        pista = pygame.image.load(r"parcial-juego\imagenes\half_uno_y_uno.png")#Imprimimos en pantalla un muñeco azul y uno rojo.
                        pista_final = pygame.transform.scale(pista,(200,100))
                        ventana.blit(pista_final,(300,250))
                        clickeado= True
                        comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 and int(pregunta_elegida[2]) == 80 :#Si se clickea en la zona donde esta ubicado el boton de comodin (half) y la cantidad de votantes azules es de cuatro...
                        pista = pygame.image.load(r"parcial-juego\imagenes\half_dos_azules.png")#Imprimimos en pantalla dos muñecos azules.
                        pista_final = pygame.transform.scale(pista,(200,100))
                        ventana.blit(pista_final,(300,250))
                        clickeado= True
                        comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                    if event.button == 1 and x >=750 and x <=810 and y >=470 and y<=530 and int(pregunta_elegida[2]) == 100 :#Si se clickea en la zona donde esta ubicado el boton de comodin (half) y la cantidad de votantes azules es de cinco...
                        pista = pygame.image.load(r"parcial-juego\imagenes\half_dos_azules.png")
                        pista_final = pygame.transform.scale(pista,(200,100))
                        ventana.blit(pista_final,(300,250))#Imprimimos en pantalla dos muñecos azules.
                        clickeado= True
                        comodin_half_usado = True#Marcamos que fue usado el comodin half para que no sea reutilizado.
                except: #En caso de un error en tiempo de ejecucion...
                    break#Detiene la ejecucion.
            if event.type == pygame.MOUSEBUTTONDOWN and user_answer =="" and comodin_reload_usado == False  :#Si recibe un evento de que se hizo click, el comodin (reload) no fue usado y el usuario no dio respuesta...
                try:
                    x=event.pos[0]
                    y=event.pos[1]
                    if event.button == 1 and x >=850 and x <=910 and y >=470 and y<=530 :#Si se clickea en la zona donde esta ubicado el boton de comodin (reload)...
                        comodin_reload_usado = True#Marcamos que fue usado el comodin reload para que no sea reutilizado.
                        tiempo_final = 0#Restablecemos el tiempo
                        ventana.blit(fondo,(0,0))
                        puntos = fuente.render(f"Puntaje: {puntaje}",True,AZUL,ROJO)
                        ventana.blit(puntos,(600,120))
                        numero = numero_random(lista_preguntas)#Elegimos un nuevo numero aleatorio.
                        pregunta_elegida = elegir_pregunta(lista_preguntas,numero)#Elegimos una nueva pregunta
                        print(pregunta_elegida)
                        pregunta_impresa = fuente.render(str(pregunta_elegida[0]),True,AZUL_CLARO,BLANCO)
                        ventana.blit(pregunta_impresa,(100,200))#Imprimimos la pregunta nueva.
                        valor_rojo = pregunta_elegida[3]#Reasignamos los valores del boton rojo en base a la nueva pregunta elegida.
                        valor_azul = pregunta_elegida[4]#Reasignamos los valores del boton azul en base a la nueva pregunta elegida.
                        rojo_impreso = fuente.render(str(valor_rojo),True,BLANCO,ROJO)
                        azul_impreso = fuente.render(str(valor_azul),True,BLANCO,AZUL)
                        #Imprimimos en la pantalla los botones.
                        ventana.blit(rojo_impreso,(250,400))
                        ventana.blit(azul_impreso,(500,400))
                        ventana.blit(boton_rojo_imagen,(250,320))
                        ventana.blit(boton_azul_imagen,(500,320))
                        boton_next = pygame.image.load(r"parcial-juego\imagenes\next.png")
                        boton_next = pygame.transform.scale(boton_next, (60,60))
                        boton_half = pygame.image.load(r"parcial-juego\imagenes\half.png")
                        boton_half = pygame.transform.scale(boton_half,(60,60))
                        boton_reload = pygame.image.load(r"parcial-juego\imagenes\reload.png")
                        boton_reload = pygame.transform.scale(boton_reload,(60,60))
                        texto_next = fuente.render("Next",True,BLANCO,NEGRO)
                        texto_half = fuente.render("Half",True,BLANCO,NEGRO)
                        texto_reload = fuente.render("Reload",True,BLANCO,NEGRO)
                        #Los botones de los comodines son solamente mostrados en pantalla si no fueron usados.
                        if comodin_next_usado == False:
                            ventana.blit(texto_next,(650,550))
                            ventana.blit(boton_next,(650,470))
                        if comodin_half_usado == False:
                            ventana.blit(boton_half,(750,470))
                            ventana.blit(texto_half,(750,550))
                        if comodin_reload_usado == False:
                            ventana.blit(boton_reload,(850,470))
                            ventana.blit(texto_reload,(850,550))
                        
                        clickeado= True
                        
                        
                except:#Si hay un error en tiempo de ejecucion...
                    break#Detenemos la ejecucion.
        if clickeado == True and user_answer !="" and user_answer != str(pregunta_elegida[1] ) or tiempo_final > 15.00 :#Si la respuesta del usuario no coincide con la correcta o el tiempo supera llos 15 segundos...
            try:
                bandera_juego_terminado = True #Se termina el juego
                tiempo_final = 0
                ventana.blit(fondo_game_over,(0,0))#Imprimimos en pantalla el fondo de game over.
                puntos = fuente.render(f"Puntaje Final: {puntaje}",True,AZUL,ROJO)
                ventana.blit(puntos,(400,500))#Imprimimos en pantalla el volumen final.
                #lista_puntajes.append(puntaje)
                
                #Sonido
                pygame.mixer.music.load(r"parcial-juego\audios\incorrecto.mp3")#Cargamos el sonido.
                pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
                pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
                
                pygame.display.update()#Actualizamos la pantalla.
            except:#Si hay un error en tiempo de ejecucion...
                break#Detenemos la ejecucion.
        if bandera_juego_terminado == True:
            escribir_puntaje(puntaje)
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 0:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 0...
            ventana.blit(fondo,(0,0))
            #Textos e iconos.
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\cero_azules.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))
            
            user_answer = ""#Reiniciamos la variable de la respuesta del usuario.
            puntaje = puntaje + 10 #Sumamos 10 puntos
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            #Tiempo
            #reiniciamos el tiempo
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            
            pygame.display.update()
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 20:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 1...
            ventana.blit(fondo,(0,0))
            #Texto e iconos.
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\uno_azul.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))
            
            user_answer = ""#Reiniciamos la variable de la respuesta del usuario.
            puntaje = puntaje + 10#Sumamos 10 puntos.
            #Tiempo
            #Reiniciamos el tiempo
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            
            pygame.display.update()#Actualizamos la pantalla.
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 40:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 2...
            ventana.blit(fondo,(0,0))
            #Textos e iconos.
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\dos_azules.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))
            
            user_answer = ""#Reiniciamos la variable de respuesta del usuario.
            puntaje = puntaje + 10#Sumamos 10 puntos.
            #Tiempo
            #Reiniciamos el tiempo.
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            
            pygame.display.update()#Actualizamos la pantalla.
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 60:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 3...
            ventana.blit(fondo,(0,0))
            #Texto e iconos.
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\tres_azules.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))
            
            user_answer = ""#Reiniciamos la variable de la respuesta del usuario.
            puntaje = puntaje + 10 #Sumamos 10 puntos
            #Tiempo
            #Reiniciamos el tiempo.
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            
            pygame.display.update()#Actualizamos la pantalla.
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 80:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 4...
            ventana.blit(fondo,(0,0))
            #Texto e iconos
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\cuatro_azules.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))#(x,y)
            
            user_answer=""#Reiniciamos la variable de respuesta del usuario.
            puntaje = puntaje + 10#Sumamos 10 puntos.
            #Tiempo
            #Reiniciamos el tiempo
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            
            pygame.display.update()#Actualizamos la pantalla.
        if clickeado == True and user_answer == str(pregunta_elegida[1]) and int(pregunta_elegida[2]) == 100:#Si el usuario hizo click y la respuesta coincide y la cantidad de votantes azules es de 5...
            ventana.blit(fondo,(0,0))
            #Texto e iconos.
            cartel= fuente.render("presiona enter para mostrar la siguiente pregunta",True,AZUL,ROJO)
            ventana.blit(cartel,(155,50))
            icono = pygame.image.load(r"parcial-juego\imagenes\cinco_azules.png")
            icono_final = pygame.transform.scale(icono,(200,100))
            texto_correcto = fuente.render("Correcto",True,ROJO,AZUL)
            ventana.blit(texto_correcto,(550,300))
            ventana.blit(icono_final,(300,250))#(x,y)
            
            user_answer = ""#Reiniciamos la variable de respuesta del usuario.
            puntaje = puntaje + 10#sumamos 10 puntos
            #Tiempo
            #Reiniciamos el tiempo.
            tiempo_transcurrido =0
            tiempo_inicial =pygame.time.get_ticks()
            tiempo_actual =pygame.time.get_ticks()
            #Sonido
            pygame.mixer.music.load(r"parcial-juego\audios\correcto.mp3")#Cargamos el audio de respuesta correcta.
            pygame.mixer.music.play(1)#Iniciamos el sonido en uno para que se repita solo una vez.
            pygame.mixer.music.set_volume(0.1)#Establecemos el volumen.
            
            pygame.display.update()#Actualizamos la pantalla.
    
pygame.display.update()#Actualizamos la pantalla.
pygame.quit()#Salimos del juego.
