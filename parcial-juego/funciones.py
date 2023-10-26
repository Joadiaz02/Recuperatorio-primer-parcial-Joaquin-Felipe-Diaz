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

def print_pregunta(pregunta: dict):
    if pregunta["bandera"] == False:
        pregunta_texto =pregunta["question"]
        #pregunta["question"]
        pregunta["bandera"] = True
        return pregunta_texto

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

def respuesta_correcta(lista:list, numero:int):
    #numero = numero_random(lista_preguntas)
    #for i in range(len(lista)):    
    #    if i == numero:
    for pregunta in lista:
        if numero==pregunta["indice"] and pregunta["bandera"] == False:
            pregunta["bandera"] = True
            respuesta_elegida = pregunta["correct_answer"]
    return respuesta_elegida
def valor_correcto(lista:list, numero:int):
    #numero = numero_random(lista_preguntas)
    #for i in range(len(lista)):    
    #    if i == numero:
    for pregunta in lista:
        if pregunta["indice"]==numero and pregunta["bandera"] == False:
            pregunta["bandera"] = True
            valor = pregunta["valor_azul"]
    return valor
numero = numero_random(lista_preguntas)
#print(numero)
lista=elegir_pregunta(lista_preguntas,numero)
#print(str(lista[2]))


#print(respuesta_correcta(lista_preguntas,numero))
#print(valor_correcto(lista_preguntas,numero))
def print_pregunta2(pregunta:dict):
    numero = numero_random(lista_preguntas)

def validar_respuesta (user_answer:str) -> bool:
    if user_answer == "rojo" or user_answer == "azul":
        retorno_validacion = False
    else:
        retorno_validacion = True
    return retorno_validacion

def print_opciones (pregunta:dict):
    opciones_rojo = pregunta["rojo"]
    opciones_azul = pregunta["azul"]
