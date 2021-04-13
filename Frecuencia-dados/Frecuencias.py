# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
print("Ingrese el numero lanzamientos: ", end="")
numero_lanzamientos = int(input())

sumatorias=[]
for i in range(numero_lanzamientos):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sumatorias.append(a+b)
    
def contar_veces(elemento, lista):
    veces = 0
    for i in lista:
        if elemento == i:
            veces += 1
    return veces

valores=[2,3,4,5,6,7,8,9,10,11,12]
frecuencias=[]
for i in valores:
    frecuencias.append(contar_veces(i,sumatorias))

print(valores,"\n", frecuencias)

import matplotlib.pyplot as plot
intervalos = range(min(valores), max(valores)+2)
plot.hist(x=sumatorias, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plot.title('Frecuencias Sumatorias')
plot.xlabel('Sumatoria')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)

plot.show()