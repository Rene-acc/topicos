
import pandas as pd
import csv

lista=[]

with open('EntrenarRed.csv')as datos:
    entrada=csv.reader(datos)
    
    lista=list(entrada, delimiter=',')

for linea in lista:
    feliz = int(linea['feliz'])
    cumpleanos = int(linea['cumpleanos'])
    amor = int (linea['amor'])
    enamorado = int (linea['enamorado'])
    musica = int (linea['musica'])
    party = int (linea['party'])
    hermoso = int (linea['hermoso'])
    bonito = int (linea['bonito'])
    vida = int (linea['vida'])
    lindo = int (linea['lindo'])
    amigos = int (linea['amigos'])
    love = int (linea['love'])
    output = int (linea['output'])
    #print(linea)
    print(feliz)
    entrad = [feliz, cumpleanos, amor, enamorado, musica, party, hermoso, bonito, vida, lindo, amigos, love]
    Entradas = pd.array(entrad)
    #print(Entradas)