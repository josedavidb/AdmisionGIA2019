#Integrantes: Jose Basanta
#             Orlando Chaparro

#Importar librerias

import numpy as np   #Libreria para arreglos, cv2 depende de ella
import cv2           #Libreria para procesar imagenes
import random        #Libreria para generar numeros random

#Clase Poligono (triangulo)
class Poligono(object):
    def __init__(self,vertice1=[0,0],vertice2=[0,0],vertice3=[0,0], color=(0,0,0)):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        self.color = color

#Crear un poligono con coordenadas de vertice y colores random
#Devuelve un objeto Poligono
def crearPoligonoRandom():
    vertice1 = [random.randint(0,512),random.randint(0,512)]
    vertice2 = [abs(vertice1[0] - random.randint(vertice1[0],vertice1[0] + 100)), abs(vertice1[0] - random.randint(vertice1[1],vertice1[1] + 100))]
    vertice3 = [random.randint(0,512),random.randint(0,512)]
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    poligono = Poligono(vertice1=vertice1,vertice2=vertice2,vertice3=vertice3,color=color)
    
    return poligono

#Dibuja un poligono en una capa del lienzo
#Recibe un lienzo (numpy array), capa_anterior (numpy array), poligono (Objeto), alpha (float)
#Alpha es el nivel de transparencia
def dibujarPoligono(lienzo,capa_anterior, poligono,alpha):
    nueva_capa = lienzo.copy()
    pts = np.array([poligono.vertice1,poligono.vertice2,poligono.vertice3],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(nueva_capa,[pts],poligono.color)
    cv2.addWeighted(nueva_capa, alpha, capa_anterior, 1 - alpha, 0,capa_anterior)

#Genera un individuo formado por Poligonos random
#Devuelve un individuo (numpy array)
def generarIndividuoRandom():
    individuo = np.zeros((512,512,3), np.uint8)
    for i in range (0,124):
        poligono = crearPoligonoRandom()
        dibujarPoligono(individuo,individuo,poligono,0.5)
    return individuo

#Genera una poblacion
#Recibe un numero (int) que es la cantidad de individuos de la poblacion
#Devuelve una poblacion (array)
def generarPoblacion(numero):
    poblacion = []
    for i in range (0,numero-1):
        individuo = generarIndividuoRandom()
        poblacion.append(individuo)
    return poblacion



#MAIN

poblacion = generarPoblacion(100)

for i in range(0,1):
    cv2.imshow('aver'+str(i),poblacion[i])
cv2.waitKey(0)
        