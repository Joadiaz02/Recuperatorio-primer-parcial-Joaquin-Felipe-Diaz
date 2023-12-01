from Lista_preguntas import * #Importamos la lista de preguntas.
import random #Importamos la libreria random 
import csv

def numero_random (lista:list):#Recibe como parametro una lista.
    lista_numeros = []#Creamos una lista donde almacenaremos los numeros obtenidos.
    largo = len(lista)#Obtenemos el largo de la lista.
    try:
        numero = random.randint(0,largo -1)#Obtenemos un numero random de la lista que recibimos por parametro.
        lista_numeros.append(numero)#Almacenamos el numero en la lista que creamos. 
    except:#Si hay un error en tiempo de ejecucion...
        for i in lista_numeros:#Recorremos la lista de numeros almacenados.
            if numero == lista_numeros[i]:#Si el numero esta en la lista...
                numero = random.randint(0,largo -1)#Obtenemos uno nuevo.
    return numero#Retorna un numero

def aplicar_bandera(lista:list):#Recibe una lista como parametro.
    for dic in lista:#Por cada diccionario en la lista.
        bandera = False
        dic["bandera"] = bandera #Asignamos la llave (bandera) con un valor de false.

def elegir_pregunta(lista:list,numero:int):#Recibe como parametro una lista y un numero.
    valores=[]#Creamos una lista donde almacenaremos los valores.
    try:
        for pregunta in lista:#Por cada pregunta de la lista
            if numero==pregunta["indice"] :#Si el numero coincide con el indice de la pregunta...
                pregunta["bandera"] = True#La bandera pasa a un estado de True.
                #Asignamos los valores de la pregunta en variables.
                pregunta_elegida = pregunta["question"]
                respuesta_elegida = pregunta["correct_answer"]
                valor = pregunta["valor_azul"]
                rojo = pregunta["rojo"]
                azul = pregunta["azul"]
                #Agregamos las variables a la lista.
                valores.append(pregunta_elegida)
                valores.append(respuesta_elegida)
                valores.append(valor)
                valores.append(rojo)
                valores.append(azul)
    except numero > 19:#Si supera el numero de indices...
        print("No existe la pregunta")#No existe la pregunta.
        
    return valores #Retorna la lista con los valores de la pregunta.


def leer_lista_puntajes():#No recibe parametros y lee un archivo csv.
    puntajes = ''
    with open('parcial-juego\puntajes.csv', newline='') as archivo_puntajes:
        data = csv.reader(archivo_puntajes,delimiter=',')
        puntajes = list(data)
    return puntajes #Retorna una lista de puntajes.


def escribir_puntaje(puntaje):#Recibe un puntaje
    with open('parcial-juego\puntajes.csv','w',newline='' ) as lista_puntajes: #Abre un archivo csv.
        lista_puntajes.write(str(puntaje))#Escribe en el archivo el nuevo valor