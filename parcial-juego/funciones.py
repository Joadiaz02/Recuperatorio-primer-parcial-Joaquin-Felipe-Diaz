from Lista_preguntas import *
import random

def numero_random (lista:list):
    lista_numeros = []
    largo = len(lista)
    try:
        numero = random.randint(0,largo -1)
        lista_numeros.append(numero)
    except:
        for i in lista_numeros:
            if numero == lista_numeros[i]:
                numero = random.randint(0,largo -1)
    return numero

def aplicar_bandera(lista:list):
    for dic in lista:
        bandera = False
        dic["bandera"] = bandera

def elegir_pregunta(lista:list,numero:int):
    #numero = numero_random(lista_preguntas)
    #for i in range(len(lista)):    
    #    if i == numero:
    valores=[]
    try:
        for pregunta in lista:
        
            if numero==pregunta["indice"] :
                pregunta["bandera"] = True
                pregunta_elegida = pregunta["question"]
                respuesta_elegida = pregunta["correct_answer"]
                valor = pregunta["valor_azul"]
                rojo = pregunta["rojo"]
                azul = pregunta["azul"]
                valores.append(pregunta_elegida)
                valores.append(respuesta_elegida)
                valores.append(valor)
                valores.append(rojo)
                valores.append(azul)
        if pregunta["bandera"] == True:
            numero = numero_random(lista)
    except:
        pregunta["bandera"]=""
    return valores


